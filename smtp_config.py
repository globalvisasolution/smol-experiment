def input_smtp_details():
    smtp_details = {}

    smtp_details['server'] = input("Enter your SMTP server: ")
    smtp_details['port'] = input("Enter your SMTP port: ")
    smtp_details['username'] = input("Enter your SMTP username: ")
    smtp_details['password'] = input("Enter your SMTP password: ")

    return smtp_details