import tkinter as tk

def colorize_interface(root):
    root.configure(bg='lightblue')

    smtp_form = tk.Entry(root, bg='lightgreen')
    smtp_form.pack()

    recipients_form = tk.Entry(root, bg='lightgreen')
    recipients_form.pack()

    message_form = tk.Text(root, bg='lightgreen')
    message_form.pack()

    send_button = tk.Button(root, text="Send Email", bg='lightgreen')
    send_button.pack()