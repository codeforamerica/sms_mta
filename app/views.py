"""
Flask Blueprint Docs:  http://flask.pocoo.org/docs/api/#flask.Blueprint

This file is used for both the routing and logic of your
application.
"""

import simplejson as json
from flask import Blueprint, render_template, redirect, request
from .sms import process

views = Blueprint('views', __name__, static_folder='../static',
                  template_folder='../templates')


@views.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@views.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@views.route('/sms', methods=['POST'])
def receive():
    """Respond to POST data received from SMSified."""
    if request.method == 'POST':
        data = json.loads(request.data)
        text = data['inboundSMSMessageNotification']['inboundSMSMessage']
        process(text)
        return "Success!"
    return redirect('/')


# The functions below should be applicable to all Flask apps.

@views.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return views.send_static_file(file_dot_text)


@views.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
