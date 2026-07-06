from roulette_game import Game
from iconButton import *
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QFont, QPixmap, QIcon
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
)

import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = None
        self.turnDecided = ""
        self.bg = Color("#576A8F")
        self.setCentralWidget(self.bg)
        self.setFixedSize(600, 300)

        self.font = QFont()
        self.font.setWeight(QFont.Weight.Bold)
        self.setWindowTitle("RouletteG")



        self.main_container = QVBoxLayout(self.bg)

        self.floating_panel = None


        self.layout1 = QHBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout2.setObjectName("QVLayout")


        self.labelHZTOP1 = QLabel("Enemy Lives: 0")
        self.labelHZTOP1.setAlignment(Qt.AlignCenter)
        self.labelHZTOP1.setStyleSheet("color: black;")
        self.labelHZTOP1.setFont(self.font)

        self.labelHZTOP2 = QLabel("Lives: 0")
        self.labelHZTOP2.setAlignment(Qt.AlignCenter)
        self.labelHZTOP2.setStyleSheet("color: black;")
        self.labelHZTOP2.setFont(self.font)

        self.layout1.addWidget(self.labelHZTOP2)


        self.layout1.addWidget(self.labelHZTOP1)

        self.label2 = QLabel("Set Opponent Lives: ")
        self.input1 = QLineEdit()
        self.label3 = QLabel("Set Lives: ")
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Max 5 lives")
        self.input1.setPlaceholderText("Max 5 lives")
        self.button = QPushButton("OK")

        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.input1)
        self.layout2.addWidget(self.label3)
        self.layout2.addWidget(self.input2)
        self.layout2.addWidget(self.button)

        self.button.clicked.connect(lambda: self.clickedAndDelete(self.layout2))
        self.button.clicked.connect(lambda: self.startGame())
        self.main_container.addLayout(self.layout1)
        self.main_container.addLayout(self.layout2) 

    def startGame(self):
        enemylives_fromUI = str(self.input1.text())
        lives_fromUI = str(self.input2.text()) 
        self.game = Game(enemylives_fromUI, lives_fromUI, False, False)
        enemyLayout = QVBoxLayout()
        playerLayout = QVBoxLayout()
        self.setUI(playerLayout, enemyLayout)
            


    def turnBtnPushed(self, playerwidget, enemylayout):
        result1 = playerwidget.objectName()
        print(result1)
        if playerwidget.objectName() == "turnBtnRock":
            self.turnDecided = "rock"
        elif playerwidget.objectName() == "turnBtnPaper":
            self.turnDecided = "paper"
        else:
            self.turnDecided = "scissor"
        self.game.player.playerTurn(self.turnDecided)
        self.game.enemy.turnShuffle()

        if self.game.enemy.enemyTurn == "rock":
            i = 1
        elif self.game.enemy.enemyTurn == "paper":
            i = 2
        else:
            i = 3
        removeP = self.layout3.takeAt(1)
        removeP.widget().deleteLater()
        removeE = self.layout3.takeAt(2)
        removeE.widget().deleteLater()
        enemywidget = enemylayout.itemAt(i).widget()
        playerIcon = playerwidget.icon()
        enemyIcon = enemywidget.icon()
        playerCpy = IconButton(playerwidget)
        playerCpy.setIcon(playerIcon)
        enemyCpy = IconButton(enemywidget)
        enemyCpy.setIcon(enemyIcon)
        self.layout3.insertWidget(1, playerCpy)
        self.layout3.insertWidget(3, enemyCpy)
        self.game.game(True)
        self.labelHZTOP1.setText(f"Opponent Lives: {str(self.game.enemy.lives)}")
        self.labelHZTOP2.setText(f"Lives: {str(self.game.player.lives)}")
        self.labelHZTOP1.update()
        self.labelHZTOP2.update()
        


        if not self.game.gameRun:
            self.setResult()
                 



    def setUI(self, playerLayout, enemyLayout):
        self.layout3 = QHBoxLayout()
        self.layout3.setObjectName("QHLayout")
        self.labelHZTOP1.setText(f"Enemy Lives: {str(self.game.enemy.lives)}")
        self.labelHZTOP2.setText(f"Live: {str(self.game.player.lives)}")
        if playerLayout:
            username = QLabel(f"{self.game.player.username}: ")
            playerLayout.addWidget(username)
            enemyName = QLabel(f"{self.game.enemy.username}: ")
            enemyLayout.addWidget(enemyName)
            
        image_path = "assets/images"
        images = ["rock.png", "paper.png", "scissor.png"]
        objName = ["rock", "paper", "scissor"]
            


        for layout in (playerLayout, enemyLayout):
            svdBtn = []
            for file, item in zip (images, objName):
                fullPath = os.path.join(image_path, file)
                pixmap = QPixmap(fullPath)
                self.turnBtn = IconButton(self)
                self.turnBtn.setIcon(QIcon(pixmap))
                self.turnBtn.setObjectName("turnBtn" + item.capitalize())
                layout.addWidget(self.turnBtn)
                saved_icon = self.turnBtn.icon()
                svdBtn.append(saved_icon)
        for i in range (1, playerLayout.count()):
            playerWidget = playerLayout.itemAt(i).widget()
            playerWidget.clicked.connect(lambda checked=False, w=playerWidget: self.turnBtnPushed(w, enemyLayout))



        InvisLabel1 = QLabel()
        InvisLabel1.hide()
        gameStartlabel = QLabel("VS")
        InvisLabel2 = QLabel()
        InvisLabel2.hide()
        gameStartlabel.setAlignment(Qt.AlignCenter)

        self.layout3.addLayout(playerLayout)
        self.layout3.addWidget(InvisLabel1)
        self.layout3.addWidget(gameStartlabel)
        self.layout3.addWidget(InvisLabel2)
        self.layout3.addLayout(enemyLayout)

        self.main_container.addLayout(self.layout3)


    def setResult(self):
        if self.floating_panel is not None:
            self.floating_panel.close()
            self.floating_panel.deleteLater()


        if self.game.gameRun == False:
            self.resultText = self.game.gameResult()
            resultTextTop = QLabel(self.resultText)
            resultTextTop.setAlignment(Qt.AlignmentFlag.AlignCenter)
            resultTextTop.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
            

            if self.resultText == "You Won":
                p = "That was too ez, dont ya think?"
            else:
                p = "Uh oh, unlucky!"
            resultText = QLabel(p)
            resultText.setAlignment(Qt.AlignmentFlag.AlignCenter)
            resultText.setStyleSheet("color: #bdc3c7; font-size: 13px;")
        else:
            return


        self.floating_panel = QWidget(self.bg)
        self.floating_panel.setStyleSheet("""
            QWidget {
                background-color: rgba(44, 62, 80, 0.95);
                border: 2px solid #34495e;
                border-radius: 12px;
            }
        """)


        self.float_layout = QVBoxLayout(self.floating_panel)
        self.float_layout.addWidget(resultTextTop)
        self.float_layout.addWidget(resultText)
        

        close_btn = QPushButton("Close", self.floating_panel)
        close_btn.setStyleSheet("background-color: #e74c3c; color: white; padding: 4px; border-radius: 4px;")
        close_btn.clicked.connect(self.floating_panel.close)
        self.float_layout.addWidget(close_btn)


        panel_w, panel_h = 280, 140
        x = int((self.bg.width() - panel_w) / 2)
        y = int((self.bg.height() - panel_h) / 2)
        self.floating_panel.setGeometry(x, y, panel_w, panel_h)


        self.floating_panel.raise_()
        self.floating_panel.show()
        

    def clickedAndDelete(self, layout):
        if layout.objectName() == "QVLayout":
            self.clear_layout(layout)
        elif layout.objectName() == "QHLayout":
            self.main_container.removeItem(layout)

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
