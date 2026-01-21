from player import Player, Enemy
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from layout_colorWidget import Color
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMenu,
)

import sys


class Game():
    def __int__(self, round, turn):
        self.round = round
        self.turn = turn
        self.enemyTurn = Enemy.doAction()
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
        
player1 = Player("Ripp", 3, "paper")

player1.doAction()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         layout1 = QHBoxLayout()
#         layout2 = QVBoxLayout()
#         layout3 = QVBoxLayout()

#         layout2.addWidget(Color('red'))
#         layout2.addWidget(Color('yellow'))
#         layout2.addWidget(Color('purple'))

#         layout1.addLayout( layout2 )

#         layout1.addWidget(Color('green'))

#         layout3.addWidget(Color('red'))
#         layout3.addWidget(Color('purple'))

#         layout1.addLayout( layout3 )

#         widget = QWidget()
#         widget.setLayout(layout1)
#         self.setCentralWidget(widget)


    
# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()
# app.exec()

