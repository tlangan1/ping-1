import smtplib
import sys

from email_constants import subject, sender, receiver
# subject = "Hello Operator, ACTION REQUIRED: Ping Failure"
# sender = "<python.ping@altisat.com>"
# receiver = "Tom.Langan@Comcast.net"

smtpObj = smtplib.SMTP( "localhost", 8025 )

def sendEmail(domain):
    print("The value of domain as passed to sendEmail is " + domain)
    # message = f"""\
    # Subject: Hi Operator
    # To: {receiver}
    # From: {sender}

    # From Ping Project without alteration from Email Project: Unfortunately the domain {domain} is not reachable."""
    message = f'Subject: {subject}\nTo: {receiver}\nFrom: {sender}\n\nFrom Ping: Unfortunately the domain, {domain}, is not reachable.'
    # print("After assigning the message variable message is: " + message)

    smtpObj.sendmail("Tom.Langan@Comcast.net", ["Tom.Langan@Comcast.net"], message)