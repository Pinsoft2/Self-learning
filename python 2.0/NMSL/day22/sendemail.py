import smtplib, ssl
import os

def email(message) :
    host = "smtp.gmail.com"
    port = 465
    username = "jjzconsultant@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")

    #"ferhetsqezetwztf"

    receiver = "jjzconsultant@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)