from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional, Dict, Any

from ..core.model import CogenBAI
from ..languages.generator import LanguageGenerator
from ..collaboration.session import SessionManager
from ..collaboration.websocket import collaboration_manager
from ..review.analyzer import CodeReviewAnalyzer
from ..testing.generator import TestGenerator

app = FastAPI(title="COGENBAI API")
model = CogenBAI()
lang_generator = LanguageGenerator()
session_manager = SessionManager()
code_reviewer = CodeReviewAnalyzer()
test_generator = TestGenerator()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class CodeRequest(BaseModel):
    prompt: str
    language: str
    framework: Optional[str] = None
    max_length: Optional[int] = 1024
    temperature: float = 0.7

@app.post("/generate")
async def generate_code(request: CodeRequest, token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
    try:
        code = model.generate_code(
            prompt=request.prompt,
            language=request.language,
            max_length=request.max_length,
            temperature=request.temperature
        )
        return {"status": "success", "code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/supported-languages")
async def get_supported_languages():
    return {"languages": list(lang_generator.language_configs.keys())}

@app.websocket("/ws/{session_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str, user_id: str):
    await collaboration_manager.connect(session_id, websocket)
    try:
        session = await session_manager.join_session(session_id, user_id)
        if not session:
            await websocket.close()
            return
            
        while True:
            data = await websocket.receive_json()
            if data["type"] == "code_update":
                await session_manager.update_code(session_id, data["code"])
                await collaboration_manager.broadcast(session_id, {
                    "type": "code_update",
                    "code": data["code"],
                    "user_id": user_id
                })
    except WebSocketDisconnect:
        await collaboration_manager.disconnect(session_id, websocket)

@app.post("/sessions/create")
async def create_session(user_id: str):
    session_id = f"session_{len(session_manager.sessions) + 1}"
    session = await session_manager.create_session(session_id, user_id)
    return session.to_dict()

@app.post("/review")
async def review_code(code: str, language: str) -> Dict[str, Any]:
    try:
        review_results = code_reviewer.review_code(code, language)
        return {"status": "success", "review": review_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-tests")
async def generate_tests(code: str, language: str, test_type: str = 'unit') -> Dict[str, str]:
    try:
        tests = test_generator.generate_tests(code, language, test_type)
        return {"status": "success", "tests": tests}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/projects/create")
async def create_project(
    name: str,
    language: str,
    framework: str,
    initial_description: str
) -> Dict[str, Any]:
    project_id = f"proj_{int(time.time())}"
    project = ProjectState(
        project_id=project_id,
        name=name,
        language=language,
        framework=framework,
        status="active",
        completion_percentage=0.0,
        last_modified=datetime.now(),
        code_snippets={},
        dependencies=[]
    )
    
    if model.project_tracker.create_project(project):
        initial_code = model.generate_code(initial_description, language, framework)
        project.code_snippets["initial"] = initial_code
        model.project_tracker.update_project(
            project_id,
            {"code_snippets": json.dumps(project.code_snippets)}
        )
        return {"status": "success", "project_id": project_id, "code": initial_code}
    
    raise HTTPException(status_code=500, detail="Failed to create project")

@app.post("/projects/{project_id}/continue")
async def continue_project(
    project_id: str,
    feature_description: str
) -> Dict[str, Any]:
    try:
        new_code = model.continue_project(project_id, feature_description)
        return {"status": "success", "code": new_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
