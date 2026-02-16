from outlook_client import OutlookClient
from email_processor import EmailProcessor
from triage_agent import TriageAgent
from jira_client import JiraClient
from issue_creator import IssueCreator
from config import Config
import utils

def main():
    print("🚀 Starting Outlook-Jira AI Agent...")
    
    # Initialize Clients
    try:
        outlook = OutlookClient()
        triage = TriageAgent()
        jira = JiraClient()
    except Exception as e:
        print(f"❌ Initialization Error: {e}")
        return
    
    # 1. Fetch Emails
    try:
        emails = outlook.fetch_emails()
        print(f"📥 Fetched {len(emails)} emails.")
    except Exception as e:
        print(f"❌ Error fetching emails: {e}")
        return

    processed_ids = utils.load_processed_ids()

    for email in emails:
        if email.id in processed_ids:
            print(f"⏩ Skipping processed email: {email.subject}")
            continue

        print(f"🔍 Processing: {email.subject}")

        # 2. Process to Markdown
        email_md = EmailProcessor.to_markdown(email)

        # 3. AI Triage
        analysis = triage.analyze(email_md)
        print(f"🤖 AI Analysis: Priority {analysis.priority} | {analysis.summary}")

        # 4. Build Issue
        jira_issue = IssueCreator.build_issue(analysis, email, Config.JIRA_PROJECT_KEY)
        
        # 5. Create in Jira
        issue_key = jira.create_issue(jira_issue)

        # 6. Mark as processed
        if issue_key:
            utils.mark_as_processed(email.id)

if __name__ == "__main__":
    main()