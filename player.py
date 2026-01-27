
import random
class Player():
    def __init__(self, username, lives, turn):
        self.username = username
        self.lives = lives
        self.turn = turn

    def playerTurn(self):
        self.turn = "rock"

class Enemy():

    def __init__(self, username, lives, enemyTurn):
        self.username = username
        self.lives = lives
        self.enemyTurn = enemyTurn
    def turnShuffle(self):
        turnShapes = ["rock", "scissor", "paper"]
        self.enemyTurn = random.choice(turnShapes)
        
    def lostTurn(self, amount):
        self.lives -= amount