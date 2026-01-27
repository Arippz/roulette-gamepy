from roulette_game import Game
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QFont
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = None
        self.bg = Color("#576A8F")
        self.setCentralWidget(self.bg)

        
        self.font = QFont()
        self.font.setWeight(QFont.Weight.Bold)
        self.setWindowTitle("RouletteG")

        self.main_container = QVBoxLayout(self.bg)


        self.layout1 = QHBoxLayout()

        self.layout2 = QVBoxLayout()
        
        self.labelHZTOP1 = QLabel("Round: 0")
        self.labelHZTOP1.setAlignment(Qt.AlignCenter)
        self.labelHZTOP1.setStyleSheet("color: black;")
        self.labelHZTOP1.setFont(self.font)
        
        self.layout1.addWidget(self.labelHZTOP1)
        
        self.labelHZTOP2 = QLabel("Lives: 0")
        self.labelHZTOP2.setAlignment(Qt.AlignCenter)
        self.labelHZTOP2.setStyleSheet("color: black;")
        self.labelHZTOP2.setFont(self.font)
        
        self.layout1.addWidget(self.labelHZTOP2)
        
        self.label2 = QLabel("Set Round: ")
        self.input1 = QLineEdit()
        self.label3 = QLabel("Set Live: ")
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Max 5 lives")
        self.input1.setPlaceholderText("Max 5 rounds")
        self.button = QPushButton("OK")

        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.input1)
        self.layout2.addWidget(self.label3)
        self.layout2.addWidget(self.input2)
        self.layout2.addWidget(self.button)

        self.button.clicked.connect(self.clickedAndDelete)
        self.button.clicked.connect(self.handleRoundClicked)

        self.main_container.addLayout(self.layout1)
        self.main_container.addLayout(self.layout2)


        

    def handleRoundClicked(self):
        round_fromUI = self.input1.text()
        lives_fromUI = self.input2.text()
        self.game = Game(round_fromUI, lives_fromUI)

        self.setUI()

    def setUI(self):
        self.labelHZTOP1.setText(f'Round: {self.game.round}')
        self.labelHZTOP2.setText(f'Live: {self.game.player.lives}')

    def clickedAndDelete(self):
        self.clear_layout(self.layout2)

        self.main_container.removeItem(self.layout2)

    def clear_layout(self, layout):
        if layout == None:
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget != None:
                widget.deleteLater()
            elif item.layout() != None:
                self.clear_layout(item.layout())


            
        


        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()

        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))

        # layout1.addLayout( layout2 )

        # layout1.addWidget(Color('green'))

        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))

        # layout1.addLayout( layout3 )

        # widget = QWidget()
        # widget.setLayout(layout1)
        # self.setCentralWidget(widget)


    
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()