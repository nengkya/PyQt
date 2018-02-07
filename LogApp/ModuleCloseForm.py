from PyQt5.QtWidgets import QWidget, QPushButton

class MainForm(QWidget): #MainForm turunan dari class QWdiget
    def __init__(self):  #self mengacu ke class MainForm
        super().__init__()
        self.setupUI()

    def setupUI(self):   #self mengacu ke class MainForm. Self harus explicit, tidak seperti this yg implicit.
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo Menutup Form')

        self.button = QPushButton('Tutup')
        self.button.move(50, 50)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
