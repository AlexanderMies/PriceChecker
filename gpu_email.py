


import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime

# Set target URL for item
URL = 'https://www.amazon.com/GeForce-RTX-2060-Architecture-GAMING/dp/B07MQ36Z6L/ref=sr_1_2?dchild=1&keywords=gtx+1080&qid=1597949838&sr=8-2'

# Chrome
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}



def check_price():
    page = requests.get(URL, headers=headers)
    now = datetime.datetime.now()

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = (soup.find(id='priceblock_ourprice').get_text())
    converted_price = int(price[1:4])

    # Price set to int
    # Had problems converting to float
    if (converted_price < 330):
        send_mail()

    # Terminal display message, needs formatting
    print('The current price of the item is: $', converted_price)
    print(title.strip())
    print('Sending message again in 2 hours')
    print('Current date and time : ')
    print (now.strftime('%Y-%m-%d %H:%M:$S'))       # Date time seconds to be fixed


def send_mail():
    # Authenticate app
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # App login and password
    server.login('alexmies95@gmail.com', 'XXXXXXXXXXXXXX')

    # Email contents
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/GeForce-RTX-2060-Architecture-GAMING/dp/B07MQ36Z6L/ref=sr_1_2?dchild=1&keywords=gtx+1080&qid=1597949838&sr=8-2'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'alexmies95@gmail.com', # Sender
        'alexmies95@gmail.com', # Recipient
        msg
    
    )

    print('Email has been sent!')

    server.quit()

# Datetime set 2 hours/7200 sec
while(True):
    check_price()
    time.sleep(7200)



