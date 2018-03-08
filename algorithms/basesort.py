#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

def victorylap(array):
    """ Runs a victory lap and peeks from the first to the last element. """
    for i in range(0, array.len()):
        array.peek(i, False, True, 0.01) # Run it slower
