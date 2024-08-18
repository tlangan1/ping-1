import smtplib

sender = "<python.ping@altisat.com>"
receiver = "Tom.Langan@Comcast.net"

message = f"""\
Subject: Hi Operator
To: {receiver}
From: {sender}

From Ping Project without alteration from Email Project: Unfortunately this domain is not reachable."""

# These credentials can be found here,
# https://mailtrap.io/inboxes/3085607/messages
user = '8c14705c6103d7'
password = 'd246138e6950f5'

def sendEmail():
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(sender, receiver, message)
        print("mail successfully sent")

sendEmail()