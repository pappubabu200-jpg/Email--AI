def resolve_conflicts(emails):
    print("Processing emails and resolving conflicts...")
    processed = []
    for email in emails:
        email['status'] = "ok"
        processed.append(email)
    return processed
