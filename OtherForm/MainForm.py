from PyQt5.QtWidgets import QWidget, QPushButton
from OtherForm import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo Menampilkan Form')

        self.button = QPushButton('Tampilkan Form Lain')
        self.button.move(50, 50)
        self.button.setParent(self)
        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.form = OtherForm()
        self.form.show()
