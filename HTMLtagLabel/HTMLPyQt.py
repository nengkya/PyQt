from PyQt5.QtWidgets import QWidget, QLabel

class TextForm(QWidget):
    def __init__(self): #self represent TextForm class
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo Tag HTML')

        #QLabel untuk menampilkan text
        self.label1 = QLabel('<h1> Hello <font color = red> PyQt </font> </h1>')
        self.label1.move(10, 10)
        self.label1.setParent(self)

        self.label2 = QLabel('Teks ini dibuat dengan tag HTML.' +
                             'Teks dapat dijadikan <i> miring </i>, dan <u> bergaris bawah </u>')
        self.label2.setWordWrap(True)
        self.label2.move(10, 50)
        self.label2.setParent(self)
