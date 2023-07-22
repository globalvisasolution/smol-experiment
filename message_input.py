def input_message():
    message_content = {}
    message_content['subject'] = input("Enter the subject of your email: ")
    message_content['body'] = input("Enter the body of your email: ")
    return message_content