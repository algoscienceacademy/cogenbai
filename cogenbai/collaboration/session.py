from typing import Dict, Set, Optional
from dataclasses import dataclass, field
from datetime import datetime
import asyncio
import json

@dataclass
class CodeSession:
    id: str
    code: str = ""
    language: str = "python"
    participants: Set[str] = field(default_factory=set)
    created_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "language": self.language,
            "participants": list(self.participants),
            "created_at": self.created_at.isoformat()
        }

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, CodeSession] = {}
        self.user_connections: Dict[str, Set[str]] = {}
        
    async def create_session(self, session_id: str, creator: str) -> CodeSession:
        session = CodeSession(id=session_id)
        session.participants.add(creator)
        self.sessions[session_id] = session
        return session
    
    async def join_session(self, session_id: str, user_id: str) -> Optional[CodeSession]:
        if session := self.sessions.get(session_id):
            session.participants.add(user_id)
            if user_id not in self.user_connections:
                self.user_connections[user_id] = set()
            self.user_connections[user_id].add(session_id)
            return session
        return None
    
    async def update_code(self, session_id: str, code: str) -> bool:
        if session := self.sessions.get(session_id):
            session.code = code
            return True
        return False
