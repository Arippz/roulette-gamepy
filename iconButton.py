from PySide6.QtWidgets import (
    QPushButton,
)

class IconButton(QPushButton):
    def resizeEvent(self, e):
        self.setFixedSize(50, 50)
        self.setIconSize(self.size())
        self.setStyleSheet("IconButton { padding-left: 0; margin: 16px; }")
        super().resizeEvent(e)
    