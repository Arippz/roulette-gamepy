from player import Player, Enemy
class Game():
    def __init__(self, enemylives, lives, turn, gameRun=False):
        super().__init__()
        self.gameRun = bool(gameRun)
        self.player = Player("Player", lives, turn)
        self.enemy = Enemy("Enemy", enemylives, turn)
    def game(self, gameRun):
        if self.player.lives > 0 or self.enemy.lives > 0:
            self.gameRun = gameRun
            while self.gameRun == True:
                if self.player.turn == "rock" and self.enemy.enemyTurn == "scissor" or \
                    self.player.turn == "scissor" and self.enemy.enemyTurn == "paper" or \
                    self.player.turn == "paper" and self.enemy.enemyTurn == "rock":
                    print(f'Your turn {self.player.turn}')
                    print(f'Opponent turn {self.enemy.enemyTurn}')
                    resultText = "You win"
                    self.enemy.lives -= 1
                    
                elif self.player.turn == self.enemy.enemyTurn:
                    print(f'Your turn {self.player.turn}')
                    print(f'Opponent turn {self.enemy.enemyTurn}')
                    resultText = "Draw"
                else:
                    print(f'Your turn {self.player.turn}')
                    print(f'Opponent turn {self.enemy.enemyTurn}')
                    resultText = "You lose"
                    self.player.lives -= 1
                if self.enemy.lives == 0 or self.player.lives == 0:
                    self.gameResult()
                return resultText
            # def gameRules(self):
    def gameResult(self):
        if self.enemy.lives == 0:
            resultText = "You Won" 
        elif self.player.lives == 0:
            resultText = "You Lost"
        self.gameRun = False
        return resultText




