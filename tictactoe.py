import os

class Game:
    def __init__(self,player_first:bool=True):
        self.running = True
        self.field = [["_","_","_"],["_","_","_"],["_","_","_"]]
        self.player = player_first

        print(f"Welcome!")
        print("".join(self.field[0] + self.field[1] + self.field[2]))
        if self.player:
            print("Your move.")
        else:
            #make move
            print("Bot started.")

        self.print_field()

        self.turn = 0
        self.run_game()

    def run_game(self):
        while self.running:
            print("Your move (\"x y\"): ",end="")
            m = input().split()
            if len(m) > 2: continue
            self.move(int(m[0]),int(m[1]))



    def print_field(self):
        print(f"Y\X \t 0   1   2")
        print(f" 0  \t {self.field[0][0]}   {self.field[0][1]}   {self.field[0][2]}")
        print(f" 1  \t {self.field[1][0]}   {self.field[1][1]}   {self.field[1][2]}")
        print(f" 2  \t {self.field[2][0]}   {self.field[2][1]}   {self.field[2][2]}")

    def move(self,x:int,y:int):
        sign = "O"
        if self.player: sign = "X"
        if x not in (0,1,2) or y not in (0,1,2): return
        if self.field[x][y] != "_": return

        self.field[x][y] = sign
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_field()
        self.player = False if self.player else True
        if self.check_winner(sign):
            print("GAME OVER!")
            self.running = False

    def check_winner(self,sign:str) -> bool:
        pattern = "".join([sign for _ in range(3)])
        lines = list()
        c = self.field[0] + self.field[1] + self.field[2]
        lines.append(c[0:3])
        lines.append(c[3:6])
        lines.append(c[6:])
        lines.append(c[0::4])
        lines.append(c[2] + c[4] + c[8])
        lines.append(c[0::3])
        lines.append(c[1::3])
        lines.append(c[2::3])
        for l in lines:
            if l == pattern: return True

        return False
