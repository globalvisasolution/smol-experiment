def input_recipients():
    recipients_emails = []
    while True:
        email = input("Enter recipient email (or 'done' to finish): ")
        if email.lower() == 'done':
            break
        recipients_emails.append(email)
    return recipients_emails