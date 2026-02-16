import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    JIRA_URL = os.getenv("JIRA_URL")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "KAN")
    
    # Azure / Outlook
    AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
    AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
    
    # Permissions required: Mail.Read
    SCOPES = ["https://graph.microsoft.com/.default"]
    AUTHORITY = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}"