# -*- coding: iso-8859-15 -*-
"""Sanity test

$Id$
"""
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

class Sanity(FunkLoadTestCase):
    """This test use a configuration file Sanity.conf."""

    def setUp(self):
        """Setting up test."""
        self.server_url = self.conf_get('main', 'url')

    def test_sanity(self):
        # The description should be set in the configuration file
        #server_url = 
        # begin of test ---------------------------------------------
        #nb_time = self.conf_getInt('test_sanity', 'nb_time')
        #for i in range(nb_time):
        self.get(self.server_url, description='Get url')
        # end of test -----------------------------------------------


if __name__ in ('main', '__main__'):
    unittest.main()
