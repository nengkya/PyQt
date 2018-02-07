import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Demo QRadioButton')

        self.label1 = QLabel('Bilangan pertama')
        self.label2 = QLabel('Bilangan kedua')
        self.numberEdit1 = QLineEdit()
        self.numberEdit2 = QLineEdit()
        
        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.numberEdit1, 0, 1)
        grid.addWidget(self.numberEdit2, 1, 1)

        self.addRadio = QRadioButton('&Tambah')

        hbox = QHBoxLayout()

        layout = QVBoxLayout()
        layout.addLayout(grid)
        self.setLayout(layout)        

a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
