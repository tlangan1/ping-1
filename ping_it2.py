import os
import sys
import time

from send_email_3 import sendEmail 

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

