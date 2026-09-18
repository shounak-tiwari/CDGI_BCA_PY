# send email using smtp module in python
# pip install smpplib 

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# ServerConfigurations 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL  = "unifyofficialteam@gmail.com"
SENDER_PASSWORD = "sumh rrvn hfby qtri"

RECIVER_EMAIL = ["yogendrabariya095@gmail.com","sidhantsingh0110@gmail.com","ginaregoutam@gmail.com","goutamchouhan029@gmail.com"]

# create a msg 
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(RECIVER_EMAIL)
msg["Subject"] = "Test email from python"
body = "Hello! this is a test email sent from python"
msg.attach(MIMEText(body,"plain"))
with smtplib.SMTP(SMTP_SERVER,SMTP_PORT)  as server:
    server.starttls() #secure the connection 
    server.login(SENDER_EMAIL,SENDER_PASSWORD)
    server.send_message(msg)
