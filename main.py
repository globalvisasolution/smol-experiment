import smtp_config
import recipient_input
import message_input
import email_sender
import interface
import animations
import colors

def main():
    smtp_details = smtp_config.input_smtp_details()
    recipients_emails = recipient_input.input_recipients()
    message_content = message_input.input_message()

    interface.smtp_form(smtp_details)
    interface.recipients_form(recipients_emails)
    interface.message_form(message_content)

    animations.animate_interface()
    colors.colorize_interface()

    send_button = interface.send_button()
    send_button.onclick = email_sender.send_email(smtp_details, recipients_emails, message_content)

if __name__ == "__main__":
    main()