#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_redrum
----------------------------------

Tests for `redrum` module.
"""

import unittest

from redrum.connections import connection


class TestConnectionManager(unittest.TestCase):

    def setUp(self):
        pass

    def test_open_connection(self):
        with connection('default') as conn:
            conn.set('mykey', 'myvalue')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
