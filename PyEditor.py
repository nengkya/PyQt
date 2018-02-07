import sys, os

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
        self.setWindowTitle('HasnaPy Editor')

        self.scriptEdit = QTextEdit('import sys')
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.scriptEdit)

        vbox3 = QVBoxLayout()
       #vbox3.addWidget(vbox2) error
        vbox3.addLayout(vbox2)

        self.exeButton    = QPushButton('&Execute')
        self.cancelButton = QPushButton('&Batal')
        hbox = QHBoxLayout()
        hbox.addStretch() #Tombol Kirim dan Batal mengecil
        hbox.addWidget(self.exeButton)
        hbox.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addLayout(vbox3)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.exeButton.clicked.connect(self.exe)

    def exe(self):
        fo = open("HasnaPyEditor.py", "w")
        mytext = self.scriptEdit.toPlainText()
        fo.write(mytext)
        os.system('python3 HasnaPyEditor.py')


a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
