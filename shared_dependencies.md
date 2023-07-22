1. "smtp_details": This is a data schema that will be shared between "main.py", "smtp_config.py", and "email_sender.py". It will contain the user's SMTP details such as server, port, username, and password.

2. "recipients_emails": This is a data schema that will be shared between "main.py", "recipient_input.py", and "email_sender.py". It will contain the list of recipient emails.

3. "message_content": This is a data schema that will be shared between "main.py", "message_input.py", and "email_sender.py". It will contain the email message that the user wants to send.

4. "send_email": This is a function name that will be shared between "main.py" and "email_sender.py". It will be responsible for sending the email.

5. "input_smtp_details": This is a function name that will be shared between "main.py" and "smtp_config.py". It will be responsible for taking the user's SMTP details as input.

6. "input_recipients": This is a function name that will be shared between "main.py" and "recipient_input.py". It will be responsible for taking the recipient emails as input.

7. "input_message": This is a function name that will be shared between "main.py" and "message_input.py". It will be responsible for taking the email message as input.

8. "animate_interface": This is a function name that will be shared between "main.py" and "animations.py". It will be responsible for animating the interface.

9. "colorize_interface": This is a function name that will be shared between "main.py" and "colors.py". It will be responsible for adding colors to the interface.

10. "smtp_form", "recipients_form", "message_form": These are id names of DOM elements that the JavaScript functions in "interface.py" will use. They correspond to the forms where the user inputs their SMTP details, recipient emails, and email message respectively.

11. "send_button": This is an id name of a DOM element that the JavaScript function in "interface.py" will use. It corresponds to the button that the user clicks to send the email.