#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

import numpy, random, threading, time
from sound import playsine

class ObjectList:
    def __init__(self, n):
        """ Creates an array of size n
        Parameters
        ----------
        n : int
            The size of the array to create.
        """
        self._size = n
        self._waittime = 0.0001
        # Creates a new zero'd array and resets eventual timers
        self.reset()
        for i in range(0, n):
            self.insert(i, float(i + 1)/n)
    def __str__(self):
        return 'Array with %d elements.' % (self.len())
    def insert(self, i, object):
        """ Inserts an element at a given position.
        Parameters
        ----------
        i : int
            The index to insert the element at.
        object : object
            The object to insert at the index.
        """
        if i > self._size or i < 0:
            raise IndexError('Index out of bounds')
        self._array[i] = object
    def reset(self):
        """ Resets the array to zero """
        self._array = numpy.empty(self._size, dtype=float)
        self._tot_peeks = 0
        self._tot_swaps = 0
    def len(self):
        """ Returns the length of the array """
        return self._size
    def settime(self, time):
        """ Sets the time to sleep between each peek in the array.
        Parameters
        ----------
        time : float
            The time to wait between each peek.
        """
        self._waittime = time
    def peek(self, i):
        """ Peeks at a given position
        Returns the attribute value of the element at the position.
        Parameters
        ----------
        i : int
            The index of the element to peek at.
        """
        if i > self.len() or i < 0:
            raise IndexError('Index out of bounds')
        self._tot_peeks += 1
        # Sleep for a small amount of time to make up for a fast processor
        time.sleep(self._waittime)
        return self._array[i]
    def swap(self, a, b, mute = False):
        """ Swaps two elements in the array.
        Parameters
        ----------
        a : int
            the index of the first element.
        b : int
            the index of the second element.
        """
        temp = self.peek(a)
        if not mute:
            playsine(50 + temp*1500, 0.1)
        self.insert(a, self.peek(b))
        self.insert(b, temp)
        self._tot_swaps += 1
    def get_peeks(self):
        """ Returns the total amount of peeks on the array """
        return self._tot_peeks
    def get_swaps(self):
        """ Returns the total amount of swaps on the array """
        return self._tot_swaps
    def shuffle(self):
        """ Shuffles all the element in the array.
            Uses the modernised version of the Fisher-Yates shuffle
        """
        for i in range(0, self.len() - 2):
            j = random.randint(i, self.len() - 1)
            self.swap(i, j, True)
        """ Reset swaps and peeks after each shuffle """
        self._tot_peeks = 0
        self._tot_swaps = 0
    def tostring(self):
        """ Prints the value of all the elements in the array. """
        print(*self._array, sep='\n')
