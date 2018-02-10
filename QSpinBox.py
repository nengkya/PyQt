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
        self.setWindowTitle('Demo QSpinBox')
        
        fontLabel = QtWidgets.QLabel()
        fontLabel.setText('Jenis huruf')

        self.fontCombo = QtWidgets.QFontComboBox()
        self.fontCombo.setEditable(False)

        sizeLabel = QtWidgets.QLabel()
        sizeLabel.setText('Ukuran huruf')

        self.sizeSpinBox = QtWidgets.QSpinBox()
        self.sizeSpinBox.setRange(8, 20)
        self.sizeSpinBox.setSingleStep(2)
        self.sizeSpinBox.setValue(18)

        self.sampleLabel = QtWidgets.QLabel()
        self.sampleLabel.setText('Contoh Teks')
        self.sampleLabel.setFont(QtGui.QFont('DejaVu Sans', 5))
        
        layout = QtWidgets.QGridLayout()
        layout.addWidget(fontLabel,        0, 0)
        layout.addWidget(self.fontCombo,   0, 1)
        layout.addWidget(sizeLabel)
        layout.addWidget(self.sizeSpinBox)
        layout.addWidget(self.sampleLabel, 2, 0, 1, 2)
        self.setLayout(layout)

        self.fontCombo.activated.connect(self.changeFont)
        self.sizeSpinBox.valueChanged.connect(self.changeFont)

    def changeFont(self):
        self.sampleLabel.setFont(QtGui.QFont(self.fontCombo.currentText(), self.sizeSpinBox.value()))

a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
