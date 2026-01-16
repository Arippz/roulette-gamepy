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
import random
# if rock == True and scissor == True:
#     scissor == False




class Player():
    def __init__(self, username, lives, turn):
        self.username = username
        self.lives = lives
        self.turn = turn

    def doAction(self, turnInput, turnInput2):
        self.turn = turnInput
        self.turn2 = turnInput2
        if self.turn == "rock" and self.turn2 == "scissor":
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.turn2}')
            print("You win")
        elif self.turn == "rock" and self.turn2 == "paper":
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.turn2}')
            print("You lose")
        else:
            print(f'Your turn {self.turn}')
            print(f'Opponent turn {self.turn2}')
            print("Draw")
        

turnShapes = ["rock", "scissor", "paper"]


player1 = Player("Ripp", 3, "rock")


player1.doAction("rock", random.choice(turnShapes))


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

