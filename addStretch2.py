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
        self.setWindowTitle('Demo QLabel, QLineEdit, dan QPushButton')

        label1 = QLabel('Bilangan pertama')
        label2 = QLabel()
        label2.setText('Bilangan kedua')
        label3 = QLabel()
        label3.setText('Hasil perhitungan')
        self.numberEdit1 = QLineEdit()
        self.numberEdit2 = QLineEdit()
        self.resultEdit  = QLineEdit()
        self.resultEdit.setReadOnly(True) #setReadOnly = bisa dicopas, setDisable(True) = abu-abu ga bisa dicopas
        
        vbox1 = QVBoxLayout()
        vbox1.addWidget(label1)
        vbox1.addWidget(self.numberEdit1)
        vbox1.addWidget(label2)
        vbox1.addWidget(self.numberEdit2)
        vbox1.addWidget(label3)
        vbox1.addWidget(self.resultEdit)

        vboxKiri = QVBoxLayout()
        vboxKiri.addLayout(vbox1)
        vboxKiri.addStretch()

        addButton       = QPushButton('&Tambah')
        substractButton = QPushButton('&Kurang')
        mulButton       = QPushButton('K&ali')
        divButton       = QPushButton('&Bagi')
        
        vbox5 = QVBoxLayout()
        vbox5.addWidget(addButton)
        vbox5.addWidget(substractButton)
        vbox5.addWidget(mulButton)
        vbox5.addWidget(divButton)
        vbox5.addStretch()

        layout = QHBoxLayout()
        layout.addLayout(vboxKiri)

        verticalLine = QFrame()
        verticalLine.setFrameShape(QFrame.VLine)
        verticalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(verticalLine)

        layout.addLayout(vbox5)
        self.setLayout(layout)

        addButton.clicked.connect(self.addButton)
        substractButton.clicked.connect(self.substractButton)
        mulButton.clicked.connect(self.mulButton)
        divButton.clicked.connect(self.divButton)

    def calculate(self, operator):
        if len(self.numberEdit1.text()) != 0 and len(self.numberEdit2.text()) != 0:
            a = float(self.numberEdit1.text())
            b = float(self.numberEdit2.text())
            if operator == '+':
                c = a + b
            elif operator == '-':
                c = a - b
            elif operator == '*':
                c = a * b
            else:
                c = a / b
            self.resultEdit.setText(str(c))

    def addButton(self):
        self.calculate('+')

    def substractButton(self):
        self.calculate('-')

    def mulButton(self):
        self.calculate('*')

    def divButton(self):
        self.calculate('/')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()
