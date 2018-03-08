#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

import numpy, random, threading, time
from sound import playsine

class Element:
    def __init__(self, height):
        self._height = height
        # Booleans for when the object is currently accessed
        self._isswap = False
        self._ispeek = False
    def value(self):
        return self._height
    def is_swapping(self):
        return self._isswap
    def is_peeking(self):
        return self._ispeek
    def set_swap(self, swap):
        self._isswap = swap
    def set_peek(self, peek):
        self._ispeek = peek
    def tostring(self):
        return str("Element: " + self._height)


class ObjectList:
    def __init__(self, n, dt = 0.0001):
        """ Creates an array of size n
        Parameters
        ----------
        n : int
            The size of the array to create.
        """
        self._size = n
        self._waittime = dt
        self._mute = False
        # Creates a new zero'd array and resets eventual timers
        """ Resets the array to zero """
        self._array = numpy.empty(self._size, dtype=object)
        self._tot_peeks = 0
        self._tot_swaps = 0
        for i in range(0, n):
            element = Element(float(i + 1)/n)
            self.insert(i, element)
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
    def len(self):
        """ Returns the length of the array """
        return self._size
    def mute(self, mute = False):
        """ Mute the application """
        self._mute = mute
    def settime(self, time):
        """ Sets the time to sleep between each peek in the array.
        Parameters
        ----------
        time : float
            The time to wait between each peek.
        """
        self._waittime = time
    def peek(self, i, getobject = False, sleep = True, dt = 0):
        """ Peeks at a given position
        Returns the attribute value of the element at the position.
        Parameters
        ----------
        i : int
            The index of the element to peek at.
        getobject : boolean
            If the returned object should be the elment or just the value
        sleep : boolean
            If the peek should sleep for a bit whilst peeking
        dt : float
            The time the peek should sleep for
        """
        if i > self.len() or i < 0:
            raise IndexError('Index out of bounds')
        self._array[i].set_peek(True)
        self._tot_peeks += 1
        # Sleep for a small amount of time to make up for a fast processor
        if sleep:
            if not dt == 0:
                if not self._mute:
                    playsine(50 + self._array[i].value()*1500, 0.1)
                time.sleep(dt)
            else:
                time.sleep(self._waittime)
        self._array[i].set_peek(False)
        if(getobject):
            return self._array[i]
        else:
            return self._array[i].value()
    def swap(self, a, b, mute = False):
        """ Swaps two elements in the array.
        Parameters
        ----------
        a : int
            the index of the first element.
        b : int
            the index of the second element.
        """
        self._array[a].set_swap(True)
        self._array[b].set_swap(True)
        temp = self.peek(a, True)
        if not mute and not self._mute:
            playsine(50 + temp.value()*1500, 0.1)
        self.insert(a, self.peek(b, True))
        self.insert(b, temp)
        self._tot_swaps += 1
        self._array[a].set_swap(False)
        self._array[b].set_swap(False)
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
