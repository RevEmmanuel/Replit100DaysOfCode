import schedule
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import env_vars

password = os.environ['mail_password']
username = os.environ['mail_username']
events_list = []
events_and_url_list = []

url = "https://replit.com/community-hub"


def check_new_event():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    my_links = soup.find_all("div", {"class": "css-wi7uht"})
    for link in my_links:
        text = link.text
        if "python" in text.lower() or "replit" in text.lower() or "intern" in text.lower():
            text = link.find_all("span")
            text = text[0].text
            if text in events_list:
                continue
            else:
                my_link = link.find_all("a")
                my_link = my_link[0]["href"]
                text_and_url = f"""
                Headline: {text}
                URL: {my_link}"""
                send_mail(text_and_url)
                events_list.append(text)
                events_and_url_list.append(text_and_url)
            

def send_mail(body):
    email = body
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = "deolaaxo@gmail.com"
    msg['From'] = username
    msg['Subject'] = "Replit Event Updates!"
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg


schedule.every(6).hours.do(check_new_event)

while True:
    schedule.run_pending()
    time.sleep(21564)
