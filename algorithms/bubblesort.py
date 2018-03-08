#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

from .basesort import victorylap

def sort(array):
    """ Bubblesort sorting function.
    Sorts an array with the bubble sorting algorithm
    Parameters
    ----------
    array : ObjectList
        array of objects to sort.
    """
    n = array.len()
    while True:
        swapped = False
        n = n - 1
        for i in range(0, n):
            if array.peek(i) > array.peek(i+1):
                array.swap(i, i + 1)
                swapped = True
        if swapped == False:
            break
    victorylap(array)
