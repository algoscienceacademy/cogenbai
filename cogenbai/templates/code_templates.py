from typing import Dict, Optional

class CodeTemplates:
    """Code templates for various programming patterns and frameworks."""
    
    def __init__(self):
        self.templates: Dict[str, Dict[str, str]] = {
            "api": {
                "python-fastapi": self._python_fastapi_template(),
                "python-flask": self._python_flask_template(),
                "node-express": self._node_express_template(),
                "go-gin": self._go_gin_template(),
                "rust-actix": self._rust_actix_template()
            },
            "cli": {
                "python-click": self._python_click_template(),
                "rust-clap": self._rust_clap_template(),
                "go-cobra": self._go_cobra_template()
            },
            "gui": {
                "python-tkinter": self._python_tkinter_template(),
                "typescript-react": self._typescript_react_template(),
                "kotlin-compose": self._kotlin_compose_template()
            }
        }
    
    def get_template(self, category: str, tech_stack: str) -> Optional[str]:
        """Get a specific template by category and technology stack."""
        return self.templates.get(category, {}).get(tech_stack)
    
    def _python_fastapi_template(self) -> str:
        return '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
'''

    def _python_flask_template(self) -> str:
        return '''
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
    app.run(debug=True)
'''

    # Add more template methods for other frameworks...
