import random
# if rock == True and scissor == True:
#     scissor == False

class Player():
    def __init__(self, username, lives, turn):
        self.username = username
        self.lives = lives
        self.turn = turn
        

class Enemy():
    turnShapes = ["rock", "scissor", "paper"]
    def __init__(self, lives, enemyTurn):
        self.lives = lives
        self.enemyTurn = enemyTurn
    
    def doAction(self):
        self.enemyTurn = random.choice(self.turnShapes)
        return self.enemyTurn