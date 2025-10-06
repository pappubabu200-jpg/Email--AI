from backend.email_reader import fetch_emails
from backend.ai_analysis import summarize_email
from backend.email_processor import resolve_conflicts
from backend.database import store_emails
from backend.retries import retry_operation

def main():
    emails = retry_operation(fetch_emails)
    if emails:
        for email in emails:
            email['summary'] = summarize_email(email['body'])
        processed_emails = resolve_conflicts(emails)
        store_emails(processed_emails)
        print("Workflow completed successfully.")

if __name__ == "__main__":
    main()
