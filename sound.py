#!/usr/bin/env python

__author__ = "Isidor Nygren, odd.meta"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

import pygame, numpy, pygame.sndarray, math
from pygame.mixer import Sound, get_init, pre_init

from array import array
from time import sleep

sound_bits = 16
sound_sample_rate = 44100
sound_max_sample = 2**(sound_bits - 1) - 1

def playsine(hz, duration):
    """ Plays a sine wave using pygame at a given frequency.
    Taken and modified from the code
    https://stackoverflow.com/questions/7816294/simple-pygame-audio-at-a-frequency
    Parameters
    ----------
    hz : int
        The frequence to play the sine wave at
    duration : float
        how long to play the sound for in seconds
    """
    n_samples = int(round(duration*sound_sample_rate))
    buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)



    for s in range(n_samples):
        t = float(s)/sound_sample_rate
        # Add amplitude smoothing at start and finish
        if s < n_samples/5:
            amp = (s)*(5/n_samples)
            buf[s][0] = int(round(sound_max_sample*math.sin(2*math.pi*hz*t)*amp))
        elif s > (4*n_samples)/5:
            amp = abs(s-n_samples)*(5/n_samples)
            buf[s][0] = int(round(sound_max_sample*math.sin(2*math.pi*hz*t)*amp)) # Left channel
        else:
            buf[s][0] = int(round(sound_max_sample*math.sin(2*math.pi*hz*t))) # Left channel
        buf[s][1] = buf[s][0] # Right channel
    sound = pygame.sndarray.make_sound(buf)
    sound.set_volume(0.05)
    sound.play(loops = 1)
