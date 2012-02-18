"""SMSified logic for the MTA application."""

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


def process(text):
    """Process an incoming text message."""
    address = text['senderAddress'].lstrip('tel:+')
    message = text['message']
    response = "Why hello there %s." % (address)
    return respond(address, response)


def respond(number, message):
    """Send an SMS text message."""
    auth = authentication()
    number = number.replace('-', '')
    params = {'address': number, 'message': message}
    sms = req.post(SEND, auth=auth, params=params)
    return sms
