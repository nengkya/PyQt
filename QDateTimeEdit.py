import sys
from PyQt5 import QtWidgets, QtCore

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
        self.dateEdit = QtWidgets.QDateEdit() #dd/mm/yy
        self.dateEdit.setDisplayFormat('dddd dd/MM/yyyy') #dddd/mm/yyyy error
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        timeLabel = QtWidgets.QLabel()
        timeLabel.setText('Waktu')

        layout = QtWidgets.QGridLayout()
        layout.addWidget(dateLabel)
        layout.addWidget(self.dateEdit)
        layout.addWidget(timeLabel)
        self.setLayout(layout)


a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
