
from PySide6.QtGui import QClipboard
from PySide6.QtWidgets import (
    QPushButton,
)


class IconButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    def resizeEvent(self, e):
        self.setFixedSize(50, 50)
        self.setIconSize(self.size())
        self.setStyleSheet("IconButton { padding-left: 0; margin: 16px; }")
        super().resizeEvent(e)
    