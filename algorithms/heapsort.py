#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

import math

def iparent(i):
    return math.floor((i-1)/2)
def ileftchild(i):
    return (2*i)+1
def ileftchild(i):
    return (2*i)+2

def siftdown(array, start, end):
    root = start
    while (ileftchild(root) <= end):
        child = ileftchild(root)
        swap = root
        if (array.peek(swap) < array.peek(child)):
            swap = child
        if (child+1) <= end and array.peek(swap) < array.peek(child + 1):
            swap = (child + 1)
        if (swap == root):
            return
        else:
            array.swap(root, swap)
            root = swap

def heapifydown(array, n):
    start = iparent(n-1)
    while (start >= 0):
        siftdown(array, start, n - 1)
        start -= 1

def siftup(array, start, end):
    child = end
    while (child > start):
        parent = iparent(child)
        if (array.peek(parent) < array.peek(child)):
            array.swap(parent, child)
            child = parent
        else:
            return

def heapifyup(array, n):
    end = 1
    while (end < n):
        siftup(array, 0, end)
        end += 1

def sort(array):
    """ Heapsort sorting function.
    Sorts an array with the heapsort algorithm
    Parameters
    ----------
    array : ObjectList
        array of objects to sort.
    """
    n = array.len()
    heapifydown(array, n)

    end = n - 1
    while (end > 0):
        array.swap(end, 0)
        end -= 1
        siftdown(array, 0, end)
