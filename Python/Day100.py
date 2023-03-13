import schedule
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import env_vars

product = {"current_price": 899_000, "buying_price": 500_000}
password = os.environ['mail_password']
username = os.environ['mail_username']
url = "https://www.jumia.com.ng/vava-furniture-imported-high-quality-massage-chair-mc988-225513582.html"


def send_mail(new_price):
    body = f"""This product is now selling for {new_price} which is below your buying price of {product["buying_price"]} """
    email = body
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg['To'] = "deolaaxo@gmail.com"
    msg['From'] = username
    msg['Subject'] = "Jumia Product Update!"
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg


def check_changes():
    data = requests.get(url)
    html = data.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.find("span", {"class": "-b -ltr -tal -fs24"})
    price = price.text
    price = price.strip()
    price = price.replace("₦", "")
    price = price.replace(" ", "")
    price = price.replace(",", "")
    price = int(price)
    if price < product["current_price"]:
        print("Cheaper")
        send_mail(price)


schedule.every(24).hours.do(check_changes)

while True:
    schedule.run_pending()
    time.sleep(86399) # 23 hours and 59 minutes
