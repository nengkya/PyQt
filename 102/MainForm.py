from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QGridLayout')

        self.label1    = QLabel('Nama')
        self.lineEdit1 = QLineEdit()

        self.label2    = QLabel('No. Handphone')
        self.lineEdit2 = QLineEdit()

        self.button1   = QPushButton('OK')

        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,    0, 0)
        self.layout.addWidget(self.lineEdit1, 0, 1)
        self.layout.addWidget(self.label2,    1, 0)
        self.layout.addWidget(self.lineEdit2, 1, 1)
       #layout.addWidget(NamaKontrol, NomorBaris, NomorKolom, RowSpan, ColumnSpan)
        self.layout.addWidget(self.button1,   2, 0, 1, 2)

        self.setLayout(self.layout)

        '''
        self.layout makes a layout inside class and store there,
        so when you call your class.layout, it returs that layout.
        Without self, it will be forgotten as soon as program leaves the scope.
        '''
