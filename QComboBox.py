import sys
from PyQt5 import QtWidgets

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QComboBox')

        self.combo = QtWidgets.QComboBox()
        for i in range(1, 11):
            self.combo.addItem('Item ke-%d' % i)    #sama
            self.combo.addItem('Item ke-' + str(i)) #sama

        getTextButton = QtWidgets.QPushButton()
        getTextButton.setText('Ambil Teks')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(getTextButton)
        layout.addStretch() #merapatkan combo dan button, dorong ke atas
        self.setLayout(layout)

        getTextButton.clicked.connect(self.getText)

    def getText(self):
        QtWidgets.QMessageBox.information(self, 'Informasi', 'Anda memilih ' + self.combo.currentText())

a = QtWidgets.QApplication(sys.argv)

form = MainForm()
form.show()

a.exec_()
