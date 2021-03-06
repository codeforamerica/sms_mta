#!/usr/bin/env python

"""Tests for the Macon Transit Authority's SMS application."""

import os
import datetime
from unittest import TestCase, main
from mock import Mock, MagicMock

import sms


class Authentication(TestCase):

    def tearDown(self):
        os.environ['SMS_USER'] = ""
        os.environ['SMS_PASS'] = ""

    def test_unconfigured_authentication(self):
        auth = sms.authentication()
        self.assertEquals(auth, ('', ''))

    def test_configured_authentication(self):
        os.environ['SMS_USER'] = "TEST"
        os.environ['SMS_PASS'] = "PASS"
        auth = sms.authentication()
        self.assertEquals(auth, ("TEST", "PASS"))


class Bus(TestCase):

    def setUp(self):
        sms.req = Mock()
        sms.json = MagicMock()
        sms.time = Mock()
        self.get = sms.req.get

    def test_help_text(self):
        text = sms.bus("HELP")
        self.assertTrue("Example" in text)

    def test_address_text(self):
        address = "1602 Montpelier Ave"
        sms.bus(address)
        self.assertTrue(self.get.called)


class FormatTime(TestCase):

    def setUp(self):
        # Cancel out any mocks
        sms.time = datetime.time

    def test_morning_time(self):
        formatted = sms.format_time("08:22")
        self.assertEqual(formatted, "08:22 AM")

    def test_afternoon_time(self):
        formatted = sms.format_time("18:27")
        self.assertEqual(formatted, "06:27 PM")


if __name__ == '__main__':
    main()
