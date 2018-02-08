import sys
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
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
        perlCheck.setText('&Perl')
        pythonCheck = QCheckBox('Python')
        rubyCheck   = QCheckBox('&Ruby')
        phpCheck    = QCheckBox('PHP')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(perlCheck)
        hbox1.addWidget(pythonCheck)
        hbox1.addWidget(rubyCheck)
        hbox1.addWidget(phpCheck)

        okButton   = QPushButton('&OK')
        exitButton = QPushButton('K&eluar')

        hbox2 = QHBoxLayout()
        hbox2.addStretch() #dorong ke kanan
        hbox2.addWidget(okButton)
        hbox2.addWidget(exitButton)
       #hbox2.addStretch() dorong ke kiri. 2 stretch = tengah-tengah

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addLayout(hbox1)
        horizontalLine = QFrame()
        horizontalLine.setFrameShape(QFrame.HLine)   #garis tebal hitam
        horizontalLine.setFrameShadow(QFrame.Sunken) #garis tipis abu bayangan
        layout.addWidget(horizontalLine) #addLayout error
        layout.addLayout(hbox2)
        self.setLayout(layout)

        def ok():
            choices = []
            if perlCheck.isChecked():
                choices.append('Perl')
            if pythonCheck.isChecked():
                choices.append('Python')
            if rubyCheck.isChecked():
                choices.append('Ruby')
            if phpCheck.isChecked():
                choices.append('PHP')

            QMessageBox.information(self, 'Informasi', repr(choices))
           #harus ada arg self.
           #QMessageBox.information(self, 'Informasi', str(choices)) hasilnya sama
           #arg3 harus string. choice = list. repr mengubah menjadi str(ing)

        okButton.clicked.connect(ok)
        exitButton.clicked.connect(self.close)

a = QApplication(sys.argv)

form = MainForm()
form.show()

a.exec()
