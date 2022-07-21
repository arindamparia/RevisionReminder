from pymongo import MongoClient
from email.message import EmailMessage
import smtplib
import datetime
import time


while True:

    CONNECTION_STRING = "mongodb+srv://arindam:Arindam9064@cluster0.lmdhr.mongodb.net/?retryWrites=true&w=majority"



    client = MongoClient(CONNECTION_STRING, connect=False)


    dbname = client['Revision_Helper']
    collection_name = dbname["data"]

    items = collection_name.find()
    todayDate = datetime.datetime.today()
    today = todayDate.strftime('%y-%m-%d')

    today='20'+today

    for item in items:

        if item['date'] == today:


            msg = EmailMessage()
            msg['Subject'] = item['topic']
            msg['From'] = 'Revison Team'
            msg['To'] = 'arindamparia321@gmail.com'
            msg.set_content(item['url'])
            server1 = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server1.login("collegereminder@gmail.com", "Arindam@9064")
            server1.send_message(msg)
            collection_name.delete_one(item)
            server1.quit()
        else:
            print("not macthed")

    time.sleep(86400)