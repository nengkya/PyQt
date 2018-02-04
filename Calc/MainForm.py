from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QFont


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Kalkulator')

        lineEdit = QLineEdit()
        lineEdit.setAlignment(Qt.AlignRight)
        lineEdit.setFont(QFont('SansSerif', 14))
        lineEdit.setDisabled(True)

        _0Button = QPushButton('0')
        _1Button = QPushButton('1')
        _2Button = QPushButton('2')
        _3Button = QPushButton('3')
        _4Button = QPushButton('4')
        _5Button = QPushButton('5')
        _6Button = QPushButton('6')
        _7Button = QPushButton('7')
        _8Button = QPushButton('8')
        _9Button = QPushButton('9')
        
        clearButton      = QPushButton('CLR')
        mulButton        = QPushButton('x')
        minusButton      = QPushButton('-')
        dotButton        = QPushButton('.')
        percentageButton = QPushButton('%')
        plusButton       = QPushButton('+')
        calculateButton  = QPushButton('=')
        
        layout = QGridLayout()
        layout.addWidget(lineEdit,    0, 0, 1, 4)
        layout.addWidget(_7Button,    1, 0)
        layout.addWidget(_8Button,    1, 1)
        layout.addWidget(_9Button,    1, 2)
        layout.addWidget(clearButton, 1, 3)
        self.setLayout(layout)
