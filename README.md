SMS MTA
=======

A work-in-progress SMS texting application to get bus times based off of
the Macon Transit Authority's schedule.

Since no real-time bus data or individual quarter-mile stop data is
currently available, and the MTA has a 90% on-time percentage, the app
will use pre-existing schedules from [the MTA's
website](http://www.mta-mac.com/schedules.html).


### Usage

All Macon public transportation is centered around an individual heading
to Terminal Station or away from Terminal Station, which plays a key
role in how the SMS app works.


### Authentication

SMSified authentication comes from the `SMS_USER` and `SMS_PASS`
environment variables -- which must be set in order for the app to work.

Locally, this can be set up with the following:

    export SMS_USER=smsified_username
    export SMS_PASS=smsified_password

For Heroku, use the `config` command.

    heroku config:add SMS_USER=smsified_username SMS_PASS=smsified_password
