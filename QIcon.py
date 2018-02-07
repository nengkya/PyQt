import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QPushButton')

        self.label = QLabel('Demo QPushButton dengan gambar icon.')

        icon1 = QIcon('add.jpeg')
        self.button1 = QPushButton('Tambah')
        self.button1.setIcon(icon1)

        icon2 = QIcon('del.png')
        self.button2 = QPushButton('Hapus')
        self.button2.setIcon(icon2)

        icon3 = QIcon('ref.ico')
        self.button3 = QPushButton('Refresh')
        self.button3.setIcon(icon3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)

a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
