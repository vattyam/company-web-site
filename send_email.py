import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "vattyam.sandeep@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "vattyam.sandeep@gmail.com"
    context = ssl.create_default_context()

#    message = """\
#    Subject : Hi!
#    Hi!
#    How are you?
 #   Bye!
 #   """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
