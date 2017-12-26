import board
import dotstar_featherwing
import time
import random

wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)

wing.clear()
wing.show()

black = (0, 0, 0)
background = (32, 8, 0)
edge = (32, 32, 0)
blue = (0, 0, 64)

row = (background, background, background, background, background, background, background, edge, black, black, black, black, black, edge, background, background, background, background, background, background, background)


for i in range(wing.rows):
	wing.shift_into_top(row, 4)
wing.show()

offset = 4
while True:
	offset = min(max(0, offset + random.randint(-1, 1)), 9)
	wing.shift_into_top(row, offset)
	if random.randint(1, 10) == 1:
		pos = random.randint(8, 12) - offset
		wing.set_color(0, pos, blue)
	wing.show()
	time.sleep(0.1)
