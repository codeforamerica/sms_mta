"""
This file is used for both the routing and logic of your
application.
"""

import os
import simplejson as json
from flask import Flask, request
from sms import process

app = Flask(__name__)


if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'this_should_be_configured'


@app.route('/', methods=['POST'])
def receive():
    """Respond to POST data received from SMSified."""
    if request.method == 'POST':
        data = json.loads(request.data)
        text = data['inboundSMSMessageNotification']['inboundSMSMessage']
        process(text)
    return "Success!"


if __name__ == '__main__':
    app.run(debug=True)
