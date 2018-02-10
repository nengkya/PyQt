import sys
from PyQt5 import QtWidgets

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QDateTimeEdit')

        dateLabel = QtWidgets.QLabel()
        dateLabel.setText('Tanggal')
        self.dateEdit = QtWidgets.QDateEdit()

        layout = QtWidgets.QGridLayout()
        layout.addWidget(dateLabel)
        layout.addWidget(self.dateEdit)
        self.setLayout(layout)


a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
