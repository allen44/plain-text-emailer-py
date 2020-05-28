import smtplib
from email.message import EmailMessage
from sys import argv

email = EmailMessage()
email['from'] = input('From:   ')
email['to'] = input('To:   ')
email['subject'] = input('Subject:   ')
email.set_content(input('Body, main text:\n'))

print(email)

try:
    username = argv[1]
    password = argv[2]
except:
    username = input('username:   ')
    password = input('Password:   ')



with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.send_message(email)
    print('all good. Message sent.')
