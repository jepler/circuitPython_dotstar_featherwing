import board
import dotstar_featherwing
import time


wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11)
starfleet = ["XXXXXXX.....",
             "..XXXXXXX...",
             "....XXXXXXX.",
             ".....XXXXXXX",
             "....XXXXXXX.",
             "..XXXXXXX..."]

wing.display_image(starfleet, (0x20, 0x20, 0x00))

time.sleep(5)

xmas = ["..y.w......w",
        "..G.....w...",
        "..G..w....w.",
        ".GGG...w....",
        "GGGGG.......",
        "wwwwwwwwwwww"]

xmas_colors = {'w': (0x20, 0x20, 0x20),
                'W': (0xFF, 0xFF, 0xFF),
                'G': (0x00, 0x20, 0x00),
                'y': (0x20, 0x20, 0x00),
                'Y': (0xFF, 0xFF, 0x00)}

wing.display_colored_image(xmas, xmas_colors)

time.sleep(5)


xmas_animation = [["..y.w......w",
                   "..G.....w...",
                   "..G..w....w.",
                   ".GGG...w....",
                   "GGGGG.......",
                   "wwwwwwwwwwww"],
                  ["..y.........",
                   "..G.W......w",
                   "..G.....w...",
                   ".GGG.w....W.",
                   "GGGGG..w....",
                   "wwwwwwwwwwww"],
                  ["..Y....W....",
                   "..G.........",
                   "..G.w......w",
                   ".GGG....w...",
                   "GGGGGw....W.",
                   "wwwwwwwwwwww"],
                  ["..y..w....w.",
                   "..G....W....",
                   "..G.........",
                   ".GGGW......w",
                   "GGGGG...w...",
                   "wwwwwwwwwwww"],
                  ["..Y.....w...",
                   "..G..w....W.",
                   "..G....w....",
                   ".GGG........",
                   "GGGGG......W",
                   "wwwwwwwwwwww"]]

while True:
	wing.display_animation(xmas_animation, xmas_colors, 10, 0.05)
                  
