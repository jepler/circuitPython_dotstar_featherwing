import board
import dotstar_featherwing
import time

wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)

# count from 0->63, shifting the binary pattern in from the right
while True:
	wing.clear()
	for x in range(64):
		wing.shift_into_right(wing.number_to_pixels(x, (0x40, 0x00, 0x00)))
		time.sleep(0.2)

