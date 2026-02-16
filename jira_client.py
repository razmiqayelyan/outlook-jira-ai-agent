import requests
from requests.auth import HTTPBasicAuth
from config import Config
from models import JiraIssue

class JiraClient:
    def __init__(self):
        self.auth = HTTPBasicAuth(Config.JIRA_EMAIL, Config.JIRA_API_TOKEN)
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.url = f"{Config.JIRA_URL}/rest/api/3/issue"

    def create_issue(self, issue: JiraIssue):
        payload = {
            "fields": {
                "project": {"key": issue.project_key},
                "summary": issue.summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"type": "text", "text": issue.description}]
                        }
                    ]
                },
                "issuetype": {"name": issue.issuetype},
                "labels": issue.labels 
            }
        }
        
        response = None
        try:
            response = requests.post(self.url, json=payload, headers=self.headers, auth=self.auth)
            response.raise_for_status()
            print(f"✅ Jira Issue Created: {response.json()['key']}")
            return response.json()['key']
        except Exception as e:
            print(f"❌ Failed to create Jira issue: {e}")
            if response:
                print(response.text)
            return None