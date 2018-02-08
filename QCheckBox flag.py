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
        self.move(400, 300)
        self.setWindowTitle('Demo QCheckBox flag')

        label = QLabel()
        label.setText('Nama file :')

        self.fileName = '/home/budi/PyQt/DemoQCheckBoxflag.py'

        self.lineEdit = QLineEdit(self.fileName)
        self.fullPathCheck = QCheckBox()
        self.fullPathCheck.setText('Nama file disertai path lengkap')
        self.fullPathCheck.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.fullPathCheck)
       #layout.addStretch() ga ngaruh
        self.setLayout(layout)

        self.fullPathCheck.clicked.connect(self.fullPath)

    def fullPath(self):
        if self.fullPathCheck.isChecked():
            self.lineEdit.setText(self.fileName)
        else:
            import ntpath, os
            s  = ntpath.basename(self.fileName)
            ss = os.path.basename(self.fileName)
            self.lineEdit.setText(ss)
           #self.lineEdit.setText(ntpath.basename(self.fileName))

a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
