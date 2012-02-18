"""
A quick Python script to use SMSified.
"""

import os
import requests as req

SEND = "https://api.smsified.com/v1/smsmessaging/outbound/4782467242/requests"

def authentication():
    """
    Get SMSified username and password authentication from environment
    variables.
    """
    username = os.environ['SMS_USER']
    password = os.environ['SMS_PASS']
    return (username, password)


def text(number, message):
    """Send an SMS text message."""
    auth = authentication()
    number = number.replace('-', '')
    params = {'address': number, 'message': message}
    sms = req.post(SEND, auth=auth, params=params)
    return sms


if __name__ == '__main__':
    sms = text('555-555-5555', "Hello, this is Macon's MTA number.")
    import pdb; pdb.set_trace()
