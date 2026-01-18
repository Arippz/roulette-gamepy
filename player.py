import random
# if rock == True and scissor == True:
#     scissor == False

class Player():
    turnShapes = ["rock", "scissor", "paper"]
    rock = 1
    scissor = 1
    paper = 1

    def __init__(self, username, lives, turn):
        self.username = username
        self.lives = lives
        self.turn = turn
        self.enemyTurn = random.choice(self.turnShapes)

    def doAction(self, turnInput):
        self.turn == turnInput
        while self.turn != 5:
            if self.turn >= "rock":
                self.rock += 5
            elif self.turn >= "scissor":
                self.scissor += 5
            else:
                self.paper += 5
            
                   


        if self.turn == self.turn and self.enemyTurn == "scissor":
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.enemyTurn}')
            print("You win")
        elif self.turn == "rock" and self.enemyTurn == "paper":
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.enemyTurn}')
            print("You lose")
        else:
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.enemyTurn}')
            print("Draw")
        




