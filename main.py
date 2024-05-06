from tictactoe import *

import itertools
import re


# do tworzenia pierwszej instancji bota
# def check_if_save(c: str) -> bool:
#     x = "XXX"
#     o = "OOO"
#     lines = []
#     lines.append(c[0:3])
#     lines.append(c[3:6])
#     lines.append(c[6:])
#     lines.append(c[0::4])
#     lines.append(c[2] + c[4] + c[8])
#     lines.append(c[0::3])
#     lines.append(c[1::3])
#     lines.append(c[2::3])
#
#     if x not in lines and o not in lines and abs(c.count("X") - c.count("O")) < 2: return True
#
#     return False


if __name__ == "__main__":
    # with open("all_input_field_states.txt", "w") as file:
    #     combinations = [''.join(x) for x in itertools.product('_XO', repeat=9)]
    #     for c in combinations:
    #         if not check_if_save(c): continue
    #
    #         file.write(c + "\n")
    game = Game(True)
