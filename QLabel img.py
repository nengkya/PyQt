import sys
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo QLabel')

        self.label1 = QLabel()
        self.label1.setText('Demo menampilkan gambar dengan QLabel')

        self.label2 = QLabel()
        self.label2.setText('<img src = PyPassContinue.png>')

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)

        self.setLayout(layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec()
