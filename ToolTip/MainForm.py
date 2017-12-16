from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo Menampilkan ToolTip')

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Ini adalah <i> tooltip </i> untuk <b> form <b>')

        self.button = QPushButton('Keluar')
        self.button.move(50, 50)
        self.button.setParent(self)
        self.button.setToolTip('Ini adalah <i> tooltip </i> untuk <b> tombol <b>')
        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
