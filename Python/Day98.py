import schedule
import os
import random
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import env_vars

password = os.environ['mail_password']
username = os.environ['mail_username']

quotes_list = []

with open("quotes.txt", "r") as file:
    data = file.read()
    quotes_list = eval(data)
    file.close()


def send_mail():
    email = random.choice(quotes_list)
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = "deolaaxo@gmail.com"
    msg['From'] = username
    msg['Subject'] = "Hourly Motivation!"
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg


schedule.every(1).hours.do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(580 * 60)
