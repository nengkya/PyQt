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
        self.addRadio.setChecked(True)
        self.substractRadio = QRadioButton()
        self.substractRadio.setText('&Kurang')
        self.substractRadio.setChecked(True)
        self.mulRadio = QRadioButton('K&ali')
        self.divRadio = QRadioButton()
        self.divRadio.setText('&Bagi')

        hbox = QHBoxLayout()
        hbox.addWidget(self.addRadio)
        hbox.addWidget(self.substractRadio)
        hbox.addWidget(self.mulRadio)
        hbox.addWidget(self.divRadio)

        self.resultLabel = QLabel()
        self.resultLabel.setText('<b> Hasil penjumlahan : </b>')
        self.calculateButton = QPushButton('&Hitung')

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.calculateButton)
       #layout.addStretch() ga ngepek
        self.setLayout(layout)

        self.addRadio.clicked.connect(lambda: self.resultLabel.setText('<b> Hasil penjumlahan : </b>'))
        self.substractRadio.clicked.connect(lambda: self.resultLabel.setText('<b> Hasil pengurangan : </b>'))
        self.mulRadio.clicked.connect(lambda: self.resultLabel.setText('<b> Hasil perkalian : </b>'))
        self.divRadio.clicked.connect(self.calculate)
        self.calculateButton.clicked.connect(self.calculate)

    def calculate(self):
        if len(self.numberEdit1.text()) != 0 and len(self.numberEdit2.text()) != 0:
            try:
                a = float(self.numberEdit1.text())
                b = float(self.numberEdit2.text())

                if self.addRadio.isChecked():
                    c = a + b
                elif self.substractRadio.isChecked():
                    c = a - b
                elif self.mulRadio.isChecked():
                    c = a * b
                else:
                    c = a / b
                    self.resultLabel.setText('<b> Hasil pembagian : </b>')

                index = self.resultLabel.text().index(':')
                s = str(self.resultLabel.text()[:index + 1])
               #self.resultLabel.setText('%s %.2f %s' % (s, c, '</b>')) #biar angka hasil bold
               #self.resultLabel.setText('%s %.2f %s' % (self.resultLabel.text(), c, '</b>')) tidak bold
                self.resultLabel.setText(self.resultLabel.text() + '<b>' + str(c) + '</b>') #unlimited fraction
            except:
                self.resultLabel.setText('Harus angka !')
            

a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
