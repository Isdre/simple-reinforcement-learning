import os
import numpy as np

class Game:
    def __init__(self,player_start:bool):
        self.running = True
        self.draw = False
        self.field = [["_","_","_"],["_","_","_"],["_","_","_"]]
        self.player = player_start

        self.bot = Bot()

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
            if self.player:
                print("Your move (\"y x\"): ", end="")
                m = input().split()
                if len(m) > 2 or (int(m[0]) > 2 or int(m[0]) < 0) or (int(m[1]) > 2 or int(m[1]) < 0): continue
                self.turn += 1
                self.move(int(m[0]), int(m[1]))
            else:
                m = self.bot.predict(self.field)
                self.move(m//3,m%3)
        z = 0
        if not self.draw:
            if self.player: z = 1 * self.turn
            else: z = -1 * (9-self.turn)
        self.bot.learn(z)
        print("GameOver")


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
            self.running = False
        else:
            if "_" not in "".join(self.field[0] + self.field[1] + self.field[2]):
                self.draw = True
                self.running = False

    def check_winner(self,sign:str) -> bool:
        pattern = sign*3
        lines = list()
        c = self.field[0] + self.field[1] + self.field[2]
        lines.append("".join(c[0:3]))
        lines.append("".join(c[3:6]))
        lines.append("".join(c[6:]))
        lines.append("".join(c[0::4]))
        lines.append("".join(c[2:7:2]))
        lines.append("".join(c[0::3]))
        lines.append("".join(c[1::3]))
        lines.append("".join(c[2::3]))
        for l in lines:
            if l == pattern: return True

        return False

class Bot:
    def __init__(self):
        self.history = []
        comb = []
        weight = []
        with open("tictactoe-bot-data.txt","r") as file:
            #input output weight
            for line in file:
                i,o,w = line.split()
                comb.append([i,o])
                weight.append(float(w))

        #create empty bot
        if len(comb) == 0:
            with open("all_input_field_states.txt", "r") as file:
                for line in file.readlines():
                    if line.count("X") < line.count("O"): continue
                    for i in [ind for ind,ele in enumerate(line) if ele == "_"]:
                        l = list(line)
                        l[i] = "O"
                        comb.append([line.rstrip(),"".join(l).rstrip()])
                        weight.append(0.0)

        self.combinations = np.array(comb)
        self.weights = np.array(weight)
        print(self.combinations)

    def predict(self,field):
        field_str = "".join(["".join(field[i]) for i in range(3)])
        possible_comb = self.combinations[np.where(self.combinations[:, 0] == field_str)]
        possible_weights = self.weights[np.where(self.combinations[:, 0] == field_str)]

        nonzero_weights = possible_weights.copy().astype(float)
        nonzero_weights += abs(possible_weights.min())
        nonzero_weights[nonzero_weights == 0] = 1e-10

        nonzero_weights /= np.sum(nonzero_weights)

        selected_row = possible_comb[np.random.choice(range(possible_comb.shape[0]), size=1,p=nonzero_weights)][0]

        self.history.append(selected_row)

        move = 0
        for a,b in zip(selected_row[0],selected_row[1]):
            if a != b: break
            move += 1

        return move

    def learn(self,z):
        #print(self.history)

        matching_indices = np.where(np.all(np.isin(self.combinations, self.history), axis=1))[0]
        print(matching_indices)

        self.weights[matching_indices] += z

        with open("tictactoe-bot-data.txt","w") as file:
            for c,w in zip(self.combinations,self.weights):
                file.write("".join(c[0]) + " " + "".join(c[1]) + " " + str(w))
                file.write("\n")