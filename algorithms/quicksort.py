#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

import random
from .basesort import victorylap

def partition(array, start, end, pivot):
    if not (start <= pivot <= end):
        raise ValueError('Pivot must be between start and end')

    array.swap(start, pivot)
    pivot = array.peek(start)
    i = start + 1
    j = start + 1

    while j <= end:
        if array.peek(j) <= pivot:
            array.swap(i,j)
            i += 1
        j += 1

    array.swap(i - 1, start)
    return i - 1

def quicksort(array, start=0, end=None):
    if end is None:
        end = array.len() - 1

    if end - start < 1:
        return

    pivot = random.randint(start, end)
    i = partition(array, start, end, pivot)

    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)

def sort(array):
    """ Quicksort sorting function.
    Sorts an array with the quicksort algorithm.
    https://stackoverflow.com/questions/17773516/in-place-quicksort-in-python
    Parameters
    ----------
    array : ObjectList
        array of objects to sort.
    """
    quicksort(array)
    victorylap(array)
