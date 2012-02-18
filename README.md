SMS MTA
=======

A work-in-progress SMS texting application to get bus times based off of
the Macon Transit Authority's schedule.

SMSified authentication comes from the `SMS_USER` and `SMS_PASS`
environment variables -- which must be set in order for the app to work.

Since no real-time bus or individual quarter-mile stop data is currently
available, and the MTA has a 90% on-time percentage, the app will use
pre-existing schedules from [the MTA's
website](http://www.mta-mac.com/schedules.html).


### Usage

All Macon public transportation is centered around an individual heading
to Terminal Station or away from Terminal Station, which plays a key
role in how the SMS app works.
