def store_emails(emails):
    print("Storing emails in database...")
    for email in emails:
        print(f"Stored: {email['subject']}")
