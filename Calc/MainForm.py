from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt #perlu untuk Qt.AlignRight pada line 19
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    def __init__(self):
       #super(MainForm, self).__init__() #harus full path class object untuk python3 -m PyInstaller
                                         #kata Pak Eko Puji Widiyanto
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Kalkulator')

        self.lineEdit = QLineEdit()
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setFont(QFont('SansSerif', 14))
        self.lineEdit.setDisabled(True)

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

        divButton        = QPushButton('/')        
        clearButton      = QPushButton('CLR')
        mulButton        = QPushButton('x')
        minusButton      = QPushButton('-')
        dotButton        = QPushButton('.')
        percentageButton = QPushButton('%')
        plusButton       = QPushButton('+')
        calculateButton  = QPushButton('=')
        
        layout = QGridLayout()
        layout.addWidget(self.lineEdit,    0, 0, 1, 4)
        layout.addWidget(_7Button,    1, 0)
        layout.addWidget(_8Button,    1, 1)
        layout.addWidget(_9Button,    1, 2)
        layout.addWidget(clearButton, 1, 3)

        layout.addWidget(_4Button,  2, 0)
        layout.addWidget(_5Button,  2, 1)
        layout.addWidget(_6Button,  2, 2)
        layout.addWidget(mulButton, 2, 3)
        
        layout.addWidget(_1Button,  3, 0)
        layout.addWidget(_2Button,  3, 1)
        layout.addWidget(_3Button,  3, 2)
        layout.addWidget(divButton, 3, 3)

        layout.addWidget(_0Button,    4, 0)
        layout.addWidget(dotButton,   4, 1)
        layout.addWidget(minusButton, 4, 2)
        layout.addWidget(plusButton,  4, 3)

        layout.addWidget(percentageButton, 5, 0)
        layout.addWidget(calculateButton,  5, 1, 1, 3)

        self.setLayout(layout)

        _0Button.clicked.connect(lambda: self.writeDigit(0))
        _1Button.clicked.connect(lambda: self.writeDigit(1))
        _2Button.clicked.connect(lambda: self.writeDigit(2))
        _3Button.clicked.connect(lambda: self.writeDigit(3))
        _4Button.clicked.connect(lambda: self.writeDigit(4))
        _5Button.clicked.connect(lambda: self.writeDigit(5))
        _6Button.clicked.connect(lambda: self.writeDigit(6))
        _7Button.clicked.connect(lambda: self.writeDigit(7))
        _8Button.clicked.connect(lambda: self.writeDigit(8))
        _9Button.clicked.connect(lambda: self.writeDigit(9))
        mulButton.clicked.connect(lambda: self.writeOperator('*'))
        divButton.clicked.connect(lambda: self.writeOperator('/'))
        plusButton.clicked.connect(lambda: self.writeOperator('+'))
        minusButton.clicked.connect(lambda: self.writeOperator('-'))
        dotButton.clicked.connect(self.writePoint)
        clearButton.clicked.connect(self.lineEdit.clear)
        calculateButton.clicked.connect(self.calculateButton)
        percentageButton.clicked.connect(self.percentageButton)

    def writeDigit(self, digit):
        if digit in range(0, 10):
            self.lineEdit.setText(self.lineEdit.text() + str(digit))

    def writeOperator(self, operator):
        if len(self.lineEdit.text()) == 0:
            return
        if operator in ['*', '/', '+', '-']:
            if self.lineEdit.text()[-1] in ['*', '/', '+', '-']:
                self.lineEdit.setText(self.lineEdit.text()[:-1] + operator)
            else:
                self.lineEdit.setText(self.lineEdit.text() + operator)

    def writePoint(self):
        if len(self.lineEdit.text()) == 0 or self.lineEdit.text()[-1] == '.':
            return
        self.lineEdit.setText(self.lineEdit.text() + '.')

    def calculateButton(self):
        expression = self.lineEdit.text()
        if len(expression) ==  0:
            return
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result)) #Kalo ga str = 'ERROR'. QLineEdit cuma terima string, bukan integer.
        except:
            self.lineEdit.setText('ERROR')

    def percentageButton(self):
        expression = self.lineEdit.text()
        if len(expression) == 0:
            return
        try:
            result = eval(expression) / 100
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')
