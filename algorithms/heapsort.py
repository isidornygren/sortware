#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

import math
from .basesort import victorylap

def heapify(array, n, i):
    end = i
    l = 2*i + 1 # Left
    r = 2*i + 2 # Right

    if l < n and array.peek(i) < array.peek(l):
        end = l
    if r < n and array.peek(end) < array.peek(r):
        end = r
    if end != i:
        array.swap(i, end)
        heapify(array, n, end)

def sort(array):
    """ Heapsort sorting function.
    Sorts an array with the heapsort algorithm
    Parameters
    ----------
    array : ObjectList
        array of objects to sort.
    """
    n = array.len()

    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array.swap(0, i)
        heapify(array, i, 0)
    victorylap(array)
