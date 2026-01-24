from player import Player, Enemy
class Game():
    def __init__(self, round):
        super().__init__()
        self.round = round
        self.turn = Player.playerTurn()
        self.enemyTurn = Enemy.turnShuffle()
    def game(self):
        if self.turn == "rock" and self.enemyTurn == "scissor" or \
            self.turn == "scissor" and self.enemyTurn == "paper" or \
            self.turn == "paper" and self.enemyTurn == "rock":
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.enemyTurn}')
            print("You win")
        elif self.turn == self.enemyTurn:
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.enemyTurn}')
            print("Draw")
        else:
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.enemyTurn}')
            print("You lose")

tes = Game(1)

tes.game()


