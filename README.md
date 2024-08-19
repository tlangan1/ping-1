# Ping with Email Python Script

## Notes

- Note that disabling internet access will not be a useful test as the email mechanism will also fail.

## Usage

- In the launch.json there is a debug configuration called "Python Debugger for ping_it.py with Arguments" that can be used to run the script. Start this debug configuration using F5 and them enter the arguments to be passed to the script. Currently that is just the `development smtp service` you want to use and `domain/ip address` that you wish to monitor. For example, to use the mailtrap smtp service and google.com you would enter `mailtrap google.com`.
- To stop the script press Shift + f5. You can also stop a script running in the bash bash terminal by setting focus to that bash terminal and pressing Ctrl + C.
- The script can also be run in a bash bash terminal as follows:
    ```
    python ping_it.py <smtp_service> <domain> 
    For example:
    python ping_it.py localhost wikipedia.org
    ```
  To stop the script launched this way set the focus to that bash terminal in which it is running if it is not already there and press Ctrl + C
- [Mailtrap](https://mailtrap.io/inboxes/3085607/messages) is where the email messages will be sent if you use that smtp service. To log into Mailtrap you will need my Github credentials.
- To use the localhost smtp service you will need to install aiosmtpd with the following command:
    ```
    pip install aiosmtpd
    ```
- To start the server open a new bash terminal and run the following command
    ```
    python -m aiosmtpd -n
    ```
    This will create a development smtp server that listens on port 8025 of localhost and will display the contents of emails sent to it in the bash terminal window in which it is running.
- When using localhost as the smtp service the email contents will show up in the bash terminal window of the bash terminal where the development smtp server, aiosmtpd is running.