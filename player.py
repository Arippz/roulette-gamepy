
import random
class Player():
    def __init__(self, username, lives, turn):
        self.username = username
        self.lives = int(lives)
        self.turn = turn

    def playerTurn(self, turnDecided):
        self.turn = turnDecided
class Enemy():
    def __init__(self, username, lives, enemyTurn):
        self.username = username
        self.lives = int(lives)
        self.enemyTurn = enemyTurn
    def turnShuffle(self):
        turnShapes = ["rock", "scissor", "paper"]
        self.enemyTurn = random.choice(turnShapes)
        

