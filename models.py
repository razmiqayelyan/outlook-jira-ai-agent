from pydantic import BaseModel
from typing import List

class EmailSchema(BaseModel):
    id: str
    subject: str
    sender: str
    body: str
    received_at: str

class TriageResult(BaseModel):
    summary: str
    description: str
    priority: str
    labels: List[str]

class JiraIssue(BaseModel):
    project_key: str
    summary: str
    description: str
    issuetype: str = "Task"
    priority: str
    labels: List[str]