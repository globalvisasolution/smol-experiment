```javascript
document.addEventListener('DOMContentLoaded', function() {
    const smtpForm = document.getElementById('smtp_form');
    const recipientsForm = document.getElementById('recipients_form');
    const messageForm = document.getElementById('message_form');
    const sendButton = document.getElementById('send_button');

    smtpForm.addEventListener('input', function() {
        window.pywebview.api.input_smtp_details(smtpForm.value);
    });

    recipientsForm.addEventListener('input', function() {
        window.pywebview.api.input_recipients(recipientsForm.value);
    });

    messageForm.addEventListener('input', function() {
        window.pywebview.api.input_message(messageForm.value);
    });

    sendButton.addEventListener('click', function() {
        window.pywebview.api.send_email();
    });

    window.pywebview.api.animate_interface();
    window.pywebview.api.colorize_interface();
});
```