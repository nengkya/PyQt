import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo QTextEdit')

        self.label1 = QLabel()
        self.label1.setText('No. HP')
        self.phoneEdit = QLineEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.phoneEdit)

        self.label2 = QLabel('Pesen')
        self.messageEdit = QTextEdit('a')
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.messageEdit)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(vbox1)
       #vbox3.addWidget(vbox2) error
        vbox3.addLayout(vbox2)

        self.sendButton   = QPushButton('&Kirim SMS')
        self.cancelButton = QPushButton('&Batal')
        hbox = QHBoxLayout()
        hbox.addStretch() #Tombol Kirim dan Batal mengecil
        hbox.addWidget(self.sendButton)
        hbox.addWidget(self.cancelButton)

        horizontalLine = QFrame()
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)

        layout = QVBoxLayout()
        layout.addLayout(vbox3)
        layout.addWidget(horizontalLine)
        layout.addLayout(hbox)
        self.setLayout(layout)


a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
