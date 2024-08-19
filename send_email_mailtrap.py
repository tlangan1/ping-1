import smtplib

subject = "Hello Operator, ACTION REQUIRED: Ping Failure"
sender = "<python.ping@altisat.com>"
receiver = "Tom.Langan@Comcast.net"

# These credentials can be found here,
# https://mailtrap.io/inboxes/3085607/messages
user = '8c14705c6103d7'
password = 'd246138e6950f5'

# message = f"""\
# Subject: Hi Operator
# To: {receiver}
# From: {sender}

# From Ping Project without alteration from Email Project: Unfortunately this domain is not reachable."""


def sendEmail(domain):
    print("The value of domain as passed to sendEmail is " + domain)
    # message = f"""\
    # Subject: Hi Operator
    # To: {receiver}
    # From: {sender}

    # From Ping Project without alteration from Email Project: Unfortunately the domain {domain} is not reachable."""
    message = f'Subject: {subject}\nTo: {receiver}\nFrom: {sender}\n\nFrom Ping: Unfortunately the domain, {domain}, is not reachable.'
    # print("After assigning the message variable message is: " + message)

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(sender, receiver, message)
        print("mail successfully sent")

# domain = "googletommy.com"
# sendEmail(domain)