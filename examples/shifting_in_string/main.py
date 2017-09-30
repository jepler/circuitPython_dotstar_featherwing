import board
import dotstar_featherwing
import time

wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)

while True:
	wing.clear()
	wing.shift_in_string(wing.font_3, "abcdefghijklmnopqrstuvwxyz0123456789!?.-_+/*=@", (0x00, 0x20, 0x20), 0.1)
	time.sleep(2)
	wing.clear()
	wing.shift_in_string(wing.font_3, "hello adafruit discord!", (0x20, 0x00, 0x20), 0.05)
	time.sleep(2)
