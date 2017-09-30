# The MIT License (MIT)
#
# Copyright (c) 2017 Dave Astels for ZombieWizard
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`dotstar_featherwing` - CircuitPython support for the 6x12 DotStar FeatherWing
====================================================

Provides a simple way to use the DotStar Feather Wing to display text, images, and animation.

* Author(s): Dave Astels
"""

import board
import adafruit_dotstar
import time

class DotstarFeatherwing:
	"""Test, Image, and Animation support for the DotStar featherwing"""
	
    blank_stripe = [(0, 0, 0),
                    (0, 0, 0),
                    (0, 0, 0),
                    (0, 0, 0),
                    (0, 0, 0),
                    (0, 0, 0)]
	"""A blank stripe, used internally to separate characters as they are shifted onto the display."""
    
    font_3 = {' ': [ 0,  0,  0],
              'A': [62, 05, 62],
              'B': [63, 37, 26],
              'C': [30, 33, 18],
              'D': [63, 33, 30],
              'E': [63, 37, 33],
              'F': [63,  5,  1],
              'G': [30, 41, 26],
              'H': [63,  4, 63],
              'I': [33, 63, 33],
              'J': [33, 31,  1],
              'K': [63,  4, 59],
              'L': [63, 32, 32],
              'M': [63,  2, 63],
              'N': [63, 12, 63],
              'O': [30, 33, 30],
              'P': [63,  5,  2],
              'Q': [30, 33, 62],
              'R': [63,  5, 58],
              'S': [18, 37, 26],
              'T': [ 1, 63,  1],
              'U': [31, 32, 63],
              'V': [31, 32, 31],
              'W': [63, 16, 63],
              'X': [59,  4, 59],
              'Y': [ 3, 60,  3],
              'Z': [49, 45, 35],
              '0': [30, 33, 30],
              '1': [34, 63, 32],
              '2': [50, 41, 38],
              '3': [33, 37, 26],
              '4': [ 7,  4, 63],
              '5': [23, 37, 25],
              '6': [30, 41, 25],
              '7': [49,  9,  7],
              '8': [26, 37, 26],
              '9': [38, 41, 30],
              '!': [ 0, 47,  0],
              '?': [ 2, 41,  6],
              '.': [ 0, 32,  0],
              '-': [ 8,  8,  8],
              '_': [32, 32, 32],
              '+': [ 8, 28,  8],
              '/': [48,  12,  3],
              '*': [20,  8, 20],
              '=': [20, 20, 20],
              'UNKNOWN': [63, 33, 63] }
	"""A sample font that uses 3 pixel wide characters."""


    def __init__(self, clock, data, brightness=1.0):
		"""Create an interface for the display.

		   :param pin clock: The clock pin for the featherwing
		   :param pin data: The data pin for the featherwing
		   :param float brightness: Optional brightness (0.0-1.0) that defaults to 1.0
		"""
        self.rows = 6
        self.columns = 12
        self.display = adafruit_dotstar.DotStar(clock, data, self.rows * self.columns, brightness, False)
              

	def shift_into_left(self, stripe):
		""" Shift a column of pixels into the left side of the display.

		    :param [int] stripe: A column of pixel colours
		"""
        for r in range(self.rows):
            rightmost = r * self.columns
            for c in range(self.columns - 1):
                self.display[rightmost + c] = self.display[rightmost + c + 1]
            self.display[rightmost + self.columns - 1] = stripe[r]
        self.display.show()


    def shift_into_right(self, stripe):
		""" Shift a column of pixels into the rightside of the display.

		    :param [int] stripe: A column of pixel colours
		"""
        for r in range(self.rows):
            leftmost = ((r + 1) * self.columns) - 1
            for c in range(self.columns - 1):
                self.display[leftmost - c] = self.display[(leftmost - c) -1]
            self.display[(leftmost - self.columns) + 1] = stripe[r]
        self.display.show()
                

    def number_to_pixels(self, x, colour):
		"""Convert an integer (0..63) into an array of 6 pixels.

		   :param int x: integer to convert into binary pixel values; LSB is topmost.
		   :param (int) colour: the colour to set "on" pixels to
		"""
        val = x
        pixels = []
        for b in range(self.rows):
            if val & 1 == 0:
                pixels.append((0, 0, 0))
            else:
                pixels.append(colour)
            val = val >> 1
        return pixels
            

    def character_to_numbers(self, font, char):
		"""Convert a letter to the sequence of column values to display.

		   :param {char -> [int]} font: the font to use to convert characters to glyphs
		   :param char letter: the char to convert
		"""
        return font[letter]


    def clear(self):
		"""Clear the display.
		   Does NOT update the LEDs
		"""
        self.display.fill((0,0,0))

        
    def shift_in_character(self, font, c, colour=(0x00, 0x40, 0x00), delay=0.2):
		"""Shifts a single character onto the display from the right edge.

		   :param {char -> [int]} font: the font to use to convert characters to glyphs
		   :param char c: the char to convert
		   :param (int) colour: the color to use for each pixel turned on
		   :param float delay: the time to wait between shifting in columns
		"""
		if c.upper() in font:
            matrix = self.character_to_numbers(font, c.upper())
        else:
            matrix = self.character_to_numbers(font, 'UNKNOWN')
        for stripe in matrix:
            self.shift_into_right(self.number_to_pixels(stripe, colour))
			time.sleep(delay)
        self.shift_into_right(self.blank_stripe)
		time.sleep(delay)


	def shift_in_string(self, font, s, colour=(0x00, 0x40, 0x00), delay=0.2):
		"""Shifts a string onto the display from the right edge.

		   :param {char -> [int]} font: the font to use to convert characters to glyphs
		   :param string s: the char to convert
		   :param (int) colour: the color to use for each pixel turned on
		   :param float delay: the time to wait between shifting in columns
		"""
        for c in s:
            self.shift_in_character(font, c, colour, delay)

        
    # Display an image
    def display_image(self, image, colour):
		"""Display an mono-coloured image.

		   :param [string] image: the textual bitmap, 'X' for set pixels, anything else for others
		   :param (int) colour: the colour to set "on" pixels to
		"""
        self.display_coloured_image(image, {'X': colour})
                            

    def display_coloured_image(self, image, colours):
		"""Display an multi-coloured image.

		   :param [string] image: the textual bitmap, character are looked up in colours for the 
		          corresponding pixel colour, anything not in the map is off
		   :param {char -> [int]} colours: a map of characters in the image data to colours to use
		"""
        for r in range(self.rows):
            for c in range(self.columns):
                index = r * self.columns + ((self.columns - 1) - c)
                key = image[r][c]
                if key in colours:
                    self.display[index] = colours[key]
                else:
                    self.display[index] = (0, 0, 0)
        self.display.show()
                            

    def display_animation(self, animation, colours, delay=0.1):
		"""Display a multi-coloured animation.

		   :param [[string]] animation: a list of textual bitmaps, each as described in display_coloured_image
		   :param {char -> [int]} colours: a map of characters in the image data to colours to use
		   :param float delay: the amount of time (seconds) to wait between frames
		"""
        self.clear()
        while True:
            for frame in animation:
                self.display_coloured_image(frame, colours)
                time.sleep(delay)
                    




