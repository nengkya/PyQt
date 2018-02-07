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

        self.label1 = QLabel('Bilangan pertama')
       #label1.setText('Bilangan pertama')
        self.numberEdit1 = QLineEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.numberEdit1)

        label2 = QLabel()
        label2.setText('Bilangan kedua')
        numberEdit2 = QLineEdit()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(label2)
        vbox2.addWidget(numberEdit2)

        label3 = QLabel()
        label3.setText('Hasil perhitungan')
        self.resultEdit = QLineEdit()
        self.resultEdit.setReadOnly(True)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(label3)
        vbox3.addWidget(self.resultEdit)

        vbox4 = QVBoxLayout()
        vbox4.addLayout(vbox1)
        vbox4.addLayout(vbox2)
        vbox4.addLayout(vbox3)
        vbox4.addStretch()

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
        layout.addLayout(vbox4)

        verticalLine = QFrame()
        verticalLine.setFrameShape(QFrame.VLine)
        verticalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(verticalLine)

        layout.addLayout(vbox5)
        self.setLayout(layout)

        addButton.clicked.connect(self.addButtonClick)

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

    def addButtonClick(self):
        self.calculate('+')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
