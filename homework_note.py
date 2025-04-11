# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 11:18:13 2025

@author: islam
"""

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit

class NoteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            self.windowFlags() |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setStyleSheet(
            "background: #FFFF12; color: #262627; border: 0; font-size: 16pt;"
        )

        layout = QVBoxLayout()

        buttons = QHBoxLayout()
        self.close_btn = QPushButton("x")
        self.close_btn.setStyleSheet(
            "font-weight: bold; font-size: 25px; width: 25px; height: 25px;"
        )
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.clicked.connect(self.close)
        buttons.addStretch(1)  
        buttons.addWidget(self.close_btn)
        layout.addLayout(buttons)

        self.text = QTextEdit()
        layout.addWidget(self.text)
        self.setLayout(layout)

app = QApplication()

note = NoteWindow()
note.show()
app.exec()
