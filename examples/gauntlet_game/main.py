# The MIT License (MIT)
#
# Copyright (c) 2018 Dave Astels
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
A gaunlet running game using the dotstar wing and the joy wing.
"""

import time
import random

import board
import busio
import dotstar_featherwing
import Adafruit_seesaw

i2c = busio.I2C(board.SCL, board.SDA)
ss = Adafruit_seesaw.Seesaw(i2c)
wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)

black = (0, 0, 0)
background = (32, 8, 0)
blue = (0, 0, 64)
player = (0, 255, 0)

row = (background, background, background, background,
       background, background, background, background,
       black, black, black, black, black,
       background, background, background, background,
       background, background, background, background)


def run():
    """Play the game."""

    player_position_col = 6
    score = 0
    steps = 0

    for _ in range(wing.rows):
        wing.shift_into_top(row, 4)
        wing.show()

    offset = 4

    while True:
        wing.set_color(3, player_position_col, black)
        offset = min(max(0, offset + random.randint(-1, 1)), 9)
        wing.shift_into_top(row, offset)
        if random.randint(1, 20) == 1:
            pos = random.randint(8, 12) - offset
            wing.set_color(0, pos, blue)

        joy_x = ss.analog_read(3)
        if joy_x < 256 and player_position_col > 0:
            player_delta = -1
        elif joy_x > 768 and player_position_col < 11:
            player_delta = 1
        else:
            player_delta = 0
        player_position_col += player_delta

        under_player = wing.get_color(3, player_position_col)
        if under_player == background:
            return steps, score
        elif under_player == blue:
            score += 1

        wing.set_color(3, player_position_col, player)
        wing.show()
        steps += 1
        if steps % 10 == 0:
            score += 1
        time.sleep(0.1)

while True:
    result = run()
    # got here because of a crash, so report and restart
    print 'Score: {} Steps: {}'.format(result[1], result[0])
    wing.clear()
    wing.show()
    wing.fill((255, 0, 0))
    wing.show()
    wing.clear()
    wing.show()
