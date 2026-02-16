from openai_client import OpenAIClient
from models import TriageResult

class TriageAgent:
    def __init__(self):
        self.ai = OpenAIClient()
        try:
            with open("prompts/triage_prompt.txt", "r") as f:
                self.prompt = f.read()
        except FileNotFoundError:
            self.prompt = "Analyze this email and return JSON with title, description, priority, labels."

    def analyze(self, email_markdown: str) -> TriageResult:
        result_json = self.ai.analyze_email(email_markdown, self.prompt)
        
        return TriageResult(
            summary=result_json.get("title", "No Title"),
            description=result_json.get("description", "No Description"),
            priority=result_json.get("priority", "Medium"),
            labels=result_json.get("labels", [])
        )