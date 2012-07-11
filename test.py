#!/usr/bin/env python

"""Tests for the Macon Transit Authority's SMS application."""

from unittest import TestCase, main
from mock import Mock

import app


class MTA(TestCase):

    def setUp(self):
        app.req = Mock()


if __name__ == '__main__':
    main()
