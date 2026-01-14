from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QMenu,
)

import sys

if rock == True and scissor == True:
    scissor == False

class Player():
    def __init__(self, lives):
        self.lives = lives

    def doAction(self):
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


    
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

