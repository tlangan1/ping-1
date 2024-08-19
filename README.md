# Ping with Email Python Script

## Notes

- Note that disabling internet access will not be a useful test as the email mechanism will also fail.

## Usage

- In the launch.json there is a debug configuration called "Python Debugger for ping_it.py with Arguments" that can be used to run the script. Start this debug configuration using F5 and then enter the arguments to be passed to the script. Currently that is just the `development smtp service` you want to use and `domain/ip address` that you wish to monitor. For example, to use the mailtrap smtp service and google.com you would enter `mailtrap google.com`.
- To stop the script press Shift + f5. You can also stop a script running in the bash terminal by setting focus to that terminal and pressing Ctrl + C.
- The script can also be run in a bash terminal as follows:
    ```
    python ping_it.py <smtp_service> <domain> 
    For example:
    python ping_it.py localhost wikipedia.org
    ```
  To stop the script launched this way set the focus to the terminal in which it is running, if it is not already there, and press Ctrl + C
- [Mailtrap](https://mailtrap.io/inboxes/3085607/messages) is where the email messages will be sent if you use that smtp service. To log into Mailtrap you will need my Github credentials.
- To use the localhost smtp service you will need to install aiosmtpd with the following command:
    ```
    pip install aiosmtpd
    ```
- To start the server open a new bash terminal and run the following command
    ```
    python -m aiosmtpd -n
    ```
    This will create a development smtp server that listens on port 8025 of localhost. Any emails sent to it will be displayed in the terminal window in which it is running.
