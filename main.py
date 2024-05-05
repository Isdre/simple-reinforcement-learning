from tictactoe import *

import itertools
import re

# def check_if_win(c:str) -> bool:
#     x = "XXX"
#     o = "OOO"
#     lines = []
#     lines.append(c[0:3])
#     lines.append(c[3:6])
#     lines.append(c[6:])
#     lines.append(c[0::4])
#     lines.append(c[2]+c[4]+c[8])
#     lines.append(c[0::3])
#     lines.append(c[1::3])
#     lines.append(c[2::3])
#     for l in lines:
#         if l == x or l == o: return True
#
#     return False

if __name__ == "__main__":
    # with open("tictactoe-bot-data.txt","w") as file:
    #     combinations = [''.join(x) for x in itertools.product('_XO', repeat=9)]
    #     for c in combinations:
    #         if check_if_win(c): continue
    #         file.write(c + " " + "0\n")
    game = Game(True)
