import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QCheckBox')

        label = QLabel()
        label.setText('Tentukan pilihan Anda :')

        perlCheck = QCheckBox()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(perlCheck)

        layout = QVBoxLayout()
        layout.addLayout(hbox1)
        self.setLayout(layout)

a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
