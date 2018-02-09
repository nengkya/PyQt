import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QFontComboBox')

        self.fontCombo = QtWidgets.QFontComboBox()
        self.fontCombo.setEditable(False) #agar text combo tidak bisa diganti

        self.label = QtWidgets.QLabel()
        self.label.setText('Contoh Teks')
        self.label.setFont(QtGui.QFont('Dejavu Sans', 18))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.fontCombo)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.fontCombo.activated.connect(self.fontGanti)

    def fontGanti(self):
        self.label.setFont(QtGui.QFont(self.fontCombo.currentText(), 15))

a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
