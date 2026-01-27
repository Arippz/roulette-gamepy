from player import Player, Enemy
class Game():
    def __init__(self, round, lives):
        super().__init__()
        self.round = round
        self.player = Player("Player", lives, False)
        self.enemy = Enemy("Enemy", lives, False)
    def game(self):
        if self.player.turn == "rock" and self.enemy.enemyTurn == "scissor" or \
            self.player.turn == "scissor" and self.enemy.enemyTurn == "paper" or \
            self.player.turn == "paper" and self.enemy.enemyTurn == "rock":
            print(f'Your turn {self.player.turn}')
            print(f'Opponent turn {self.enemy.enemyTurn}')
            print("You win")
            amount += 1

        elif self.player.turn == self.enemy.enemyTurn:
            print(f'Your turn {self.player.turn}')
            print(f'Opponent turn {self.enemy.enemyTurn}')
            print("Draw")
        else:
            print(f'Your turn {self.player.turn}')
            print(f'Opponent turn {self.enemy.enemyTurn}')
            print("You lose")
    
    # def gameRules(self):

        
    




