from rouletteG import Game
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

class MainWindow(QMainWindow, Game):
    def __init__(self):
        super().__init__(round=0)
        
        self.bg = Color("#576A8F")
        self.setCentralWidget(self.bg)

        
        self.font = QFont()
        self.font.setWeight(QFont.Weight.Bold)
        self.setWindowTitle("RouletteG")

        self.main_container = QVBoxLayout(self.bg)


        self.layout1 = QHBoxLayout()

        self.layout2 = QVBoxLayout()
        
        self.label1 = QLabel("Round: 0")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("color: black;")
        self.label1.setFont(self.font)
        
        self.layout1.addWidget(self.label1)

        
        self.label2 = QLabel("Set Round: ")
        self.input = QLineEdit()
        self.input.setPlaceholderText("Max 5 rounds")
        self.button = QPushButton("OK")
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.input)
        self.layout2.addWidget(self.button)

        self.button.clicked.connect(self.handleRoundClicked)

        self.main_container.addLayout(self.layout1)
        self.main_container.addLayout(self.layout2)


        

    def handleRoundClicked(self):
        data = self.input.text()
        self.gameRules(data)
        self.setUI()

    def setUI(self):
        self.label1.setText(f'Round: {self.round}')
        self.main_container.hide()

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