import sqlite3
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class ProjectState:
    project_id: str
    name: str
    language: str
    framework: str
    status: str
    completion_percentage: float
    last_modified: datetime
    code_snippets: Dict[str, str]
    dependencies: List[str]

class ProjectTracker:
    def __init__(self, db_path: str = "cogenbai_projects.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                project_id TEXT PRIMARY KEY,
                name TEXT,
                language TEXT,
                framework TEXT,
                status TEXT,
                completion_percentage REAL,
                last_modified TIMESTAMP,
                code_snippets TEXT,
                dependencies TEXT
            )
        ''')
        self.conn.commit()

    def create_project(self, project: ProjectState) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                project.project_id,
                project.name,
                project.language,
                project.framework,
                project.status,
                project.completion_percentage,
                project.last_modified.isoformat(),
                json.dumps(project.code_snippets),
                json.dumps(project.dependencies)
            ))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error creating project: {e}")
            return False

    def update_project(self, project_id: str, updates: Dict) -> bool:
        try:
            cursor = self.conn.cursor()
            set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
            query = f"UPDATE projects SET {set_clause} WHERE project_id = ?"
            cursor.execute(query, list(updates.values()) + [project_id])
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating project: {e}")
            return False

    def get_project(self, project_id: str) -> Optional[ProjectState]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM projects WHERE project_id = ?", (project_id,))
        row = cursor.fetchone()
        if row:
            return ProjectState(
                project_id=row[0],
                name=row[1],
                language=row[2],
                framework=row[3],
                status=row[4],
                completion_percentage=row[5],
                last_modified=datetime.fromisoformat(row[6]),
                code_snippets=json.loads(row[7]),
                dependencies=json.loads(row[8])
            )
        return None
