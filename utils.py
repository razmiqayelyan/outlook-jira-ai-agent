import json
import os

PROCESSED_FILE = "storage/processed_emails.json"

def load_processed_ids():
    if not os.path.exists(PROCESSED_FILE):
        return []
    try:
        with open(PROCESSED_FILE, "r") as f:
            data = json.load(f)
            return data.get("processed", [])
    except json.JSONDecodeError:
        return []

def mark_as_processed(email_id):
    ids = load_processed_ids()
    if email_id not in ids:
        ids.append(email_id)
        with open(PROCESSED_FILE, "w") as f:
            json.dump({"processed": ids}, f, indent=2)