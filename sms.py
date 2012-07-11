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


def bus(message):
    """Find the bus info associated with a given address."""
    message = message.lower().strip()
    transit = "http://transit2me.herokuapp.com/stopnear"
    if 'help' in message:
        reply = ("Text your address to get estimated bus times. "
                 "Example: 1602 Montpelier Ave. "
                 "You can also call the MTA at: 478-803-2505")
    else:
        response = req.get(transit, params={'address':message})
        if response.status_code == 500:
            reply = ("Hmm, there seems to be an error with that address. "
                     "Text HELP for example usage.")
        else:
            data = response.json
            stop = data['name']
            inbound = data['routes'][0]['intime']
            outbound = data['routes'][0]['outtime']
            reply = "Stop: %s. INBOUND: %s OUTBOUND: %s" % (stop, inbound, outbound)
    return reply


def process(text):
    """Process an incoming text message."""
    address = text['senderAddress'].lstrip('tel:+')
    message = text['message']
    info = bus(message)
    return respond(address, info)


def respond(number, message):
    """Send an SMS text message."""
    auth = authentication()
    number = number.replace('-', '')
    params = {'address': number, 'message': message}
    sms = req.post(SEND, auth=auth, params=params)
    return sms