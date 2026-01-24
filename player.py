import random
# if rock == True and scissor == True:
#     scissor == False

class Player():
    def __init__(self, username, lives, turn):
        self.username = username
        self.lives = lives

    @staticmethod
    def playerTurn():
        turn = "rock"
        return turn
class Enemy():

    def __init__(self, lives, enemyTurn):
        self.lives = lives
    
    @staticmethod
    def turnShuffle():
        turnShapes = ["rock", "scissor", "paper"]
        enemyTurn = random.choice(turnShapes)
        return enemyTurn
        
    def lostTurn(self, amount):
        self.lives -= amount