import requests
import msal
from config import Config
from models import EmailSchema

class OutlookClient:
    def __init__(self):
        self.app = msal.ConfidentialClientApplication(
            Config.AZURE_CLIENT_ID,
            authority=Config.AUTHORITY,
            client_credential=Config.AZURE_CLIENT_SECRET,
        )

    def get_token(self):
        result = self.app.acquire_token_silent(Config.SCOPES, account=None)
        if not result:
            result = self.app.acquire_token_for_client(scopes=Config.SCOPES)
        return result.get("access_token")

    def fetch_emails(self, limit=5) -> list[EmailSchema]:
        token = self.get_token()
        if not token:
            raise Exception("Failed to acquire Azure token")

        headers = {'Authorization': 'Bearer ' + token}
        
        # Graph API endpoint for user messages
        url = f"https://graph.microsoft.com/v1.0/users/{Config.JIRA_EMAIL}/messages"
        params = {
            '$top': limit,
            '$select': 'id,subject,from,body,receivedDateTime',
            '$filter': 'isRead eq false' 
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        emails = []
        for item in data.get('value', []):
            # Safe access to sender email
            sender = "Unknown"
            if item.get('from') and item['from'].get('emailAddress'):
                sender = item['from']['emailAddress']['address']

            emails.append(EmailSchema(
                id=item['id'],
                subject=item['subject'],
                sender=sender,
                body=item['body']['content'],
                received_at=item['receivedDateTime']
            ))
        return emails