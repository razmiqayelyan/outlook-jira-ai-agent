from models import JiraIssue, TriageResult, EmailSchema

class IssueCreator:
    @staticmethod
    def build_issue(triage: TriageResult, email: EmailSchema, project_key: str) -> JiraIssue:
        return JiraIssue(
            project_key=project_key,
            summary=triage.summary,
            description=f"{triage.description}\n\nOriginal Sender: {email.sender}\nOriginal Date: {email.received_at}",
            priority=triage.priority,
            labels=triage.labels
        )