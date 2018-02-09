import sys
from PyQt5 import QtWidgets

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QSpinBox()')
        
        fontLabel  = QtWidgets.QLabel()
        fontLabel.setText('Jenis huruf')

        layout = QtWidgets.QGridLayout()
        layout.addWidget(fontLabel)
        self.setLayout(layout)

a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
