from PyQt5.QtWidgets import QWidget, QPushButton

class OtherForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300, 200)
        self.move(350, 250)
        self.setWindowTitle('Form Lain')

        self.button = QPushButton('Tutup')
        self.button 
    
