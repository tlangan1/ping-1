import os
import sys
import time
import smtplib

######################################################
# Just the stuff relevant to emailing...
# Should be in a separate module, but for now, it's here.
sender = "<python.ping@altisat.com>"
receiver = "Tom.Langan@Comcast.net"

# These credentials can be found here,
# https://mailtrap.io/inboxes/3085607/messages
user = '8c14705c6103d7'
password = 'd246138e6950f5'

def sendEmail(domain):
    message = f"""\
    Subject: Hi Operator
    To: {receiver}
    From: {sender}

    From Ping Project: Unfortunately domain """ + domain + """ is not reachable."""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(sender, receiver, message)
        print("mail successfully sent")
# End of Just the stuff relevant to emailing...
######################################################

# hard-coded timing variables
success_wait_time = 1
failure_wait_time = 10

# The script can be run on the terminal as follows:
# python ping_it.py <domain>
# For example:
# python ping_it.py google.com
#
# To stop the script, press Ctrl + C

# The other test that can be done is enabling/disabling internet access
# on the machine on which the script is being executed.

domain = sys.argv[1]
print("\n\n The domain to be monitored by this process is " + domain + ".")

while True:
    print("\n****************************************************")
    print("\n\n Pinging domain: " + domain + " ...")
    output = os.popen("ping " + domain)

    return_code = output.close()

    if (return_code == None):
        print("\n Command was successful")
        print("\n Waiting for " + str(success_wait_time) + " second ...")
        time.sleep(1)
    else:
        print("\n" + str(return_code) + " Command failed sending email ...")
        sendEmail(domain)
        print("\n" + "Waiting for " + str(failure_wait_time) + " seconds ...")
        time.sleep(10)


