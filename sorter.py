#!/usr/bin/env python

__author__ = "Isidor Nygren"
__copyright__ = "Copyright 2018, Isidor Nygren"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Isidor Nygren"
__email__ = "admin@isidor.co.uk"

# from graphics import *
import pygame, sys, threading, time, math, importlib, datetime
from object_list import ObjectList
import algorithms.bubblesort as bubblesort

class Sorter:
    def __init__(self, width, height, objects, algorithm_str):
        self._width = width
        self._height = height
        # Space between the rectangles and the edges of the window
        self._window_margin = 100
        self._finished_time = 0
        # space between each rectangle
        self._rectangle_margin = 5
        self._rectangle_height = height - 2*self._window_margin
        self._rectangle_width = float(width - self._window_margin*2 - self._rectangle_margin*objects)/objects
        # Initialise array of randomised objects
        self._object_list = ObjectList(objects)
        self._object_list.shuffle()
        # Pygame for initialising graphical engine
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        self._screen.fill((0,0,0))
        pygame.display.set_caption('Sårter: %s' % (algorithm_str))
        # Create text font
        # self._font = pygame.font.SysFont('Arial', 20)
        self._font = pygame.font.Font('fonts/FiraMono-Medium.ttf', 14)
        self._algorithm_text = self._font.render('Algorithm: %s' % (algorithm_str.title()), True, (255,255,255))
        # Create sorting thread
        algorithm = importlib.import_module('algorithms.' + algorithm_str)
        # Main loop
        done = False
        first_time = True
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    # If not already running
                    if not (hasattr(self, '_sort_thread') and self._sort_thread.isAlive()):
                        # Shuffle the array
                        if not first_time:
                            self._finished_time = 0 # Reset timer
                            # Create a new empty array
                            self._object_list = ObjectList(objects)
                            self._object_list.shuffle()
                        else:
                            first_time = False
                        # Start sorting
                        self._sort_thread = threading.Thread(target=algorithm.sort, args=(self._object_list,))
                        self._sort_thread.daemon = True                            # Daemonize thread

                        self._start_time = datetime.datetime.now()
                        self._sort_thread.start()
            self.draw()
            pygame.display.flip()

    def draw(self):
        self._screen.fill((0,0,0))
        # Draw text
        self._screen.blit(self._algorithm_text, (self._width/2 - self._algorithm_text.get_width()/2, 5))
        peek_text = self._font.render("Peeks: " + str(self._object_list.get_peeks()), True, (255,255,255))
        swap_text = self._font.render("Swaps: " + str(self._object_list.get_swaps()), True, (255,255,255))
        self._screen.blit(peek_text, (5, 5))
        self._screen.blit(swap_text, (5, 22))
        if hasattr(self, '_start_time'):
            if self._sort_thread.is_alive():
                deltatime = (datetime.datetime.now() - self._start_time)
            else:
                if (self._finished_time == 0):
                    self._finished_time = datetime.datetime.now()
                deltatime = (self._finished_time - self._start_time)
            timer_text = self._font.render(str(deltatime), True, (255,255,255))
            self._screen.blit(timer_text, (self._width/2 - timer_text.get_width()/2, 22))
        # Calculate each rectangle size and position
        for (i, element) in enumerate(self._object_list._array):
            x = math.ceil(i*self._rectangle_width) + self._window_margin + self._rectangle_margin*i
            y = self._window_margin + math.ceil(self._rectangle_height - self._rectangle_height*element.value())
            height = self._rectangle_height*element.value()
            width = self._rectangle_width
            if element.is_swapping():
                color = (200,0,0)
            elif element.is_peeking():
                color = (0,200,0)
            else:
                color = (200,200,200)
            pygame.draw.rect(self._screen, color, (x, y, width, height), 0)

Sorter(1000, 500, 40, "bubblesort")
