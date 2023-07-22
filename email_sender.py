import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from smtp_config import smtp_details
from recipient_input import recipients_emails
from message_input import message_content

def send_email():
    try:
        server = smtplib.SMTP(smtp_details['server'], smtp_details['port'])
        server.starttls()
        server.login(smtp_details['username'], smtp_details['password'])

        for recipient in recipients_emails:
            msg = MIMEMultipart()
            msg['From'] = smtp_details['username']
            msg['To'] = recipient
            msg['Subject'] = "Bulk Email"
            body = message_content
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            server.sendmail(smtp_details['username'], recipient, text)

        server.quit()
        print("Emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")