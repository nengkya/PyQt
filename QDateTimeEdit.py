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
        self.timeEdit = QtWidgets.QTimeEdit()
        self.timeEdit.setTime(QtCore.QTime.currentTime())
        self.timeEdit.setDisplayFormat('hh:mm') #standard 16.07

        dateTimeLabel = QtWidgets.QLabel()
        dateTimeLabel.setText('Tanggal dan Waktu')
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat('dddd hh:mm dd/MM/yyyy') #standard 01/01/00 00.00
       #self.dateTimeEdit.setDisplayFormat('hh:mm dddd dd/mm/yyyy') error

        self.okButton = QtWidgets.QPushButton('&Ok')
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(dateLabel,     0, 0)
        layout.addWidget(self.dateEdit, 0, 1)
        layout.addWidget(timeLabel)
        layout.addWidget(self.timeEdit)
        layout.addWidget(dateTimeLabel)
        layout.addWidget(self.dateTimeEdit)
        layout.addLayout(hbox, 3, 0, 1, 2)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.ok)

    def ok(self):
        QtWidgets.QMessageBox.information(self, 'Informasi',
                                          'Date : '     + self.dateEdit.date().toString() + '\n' +
                                          'Time : '     + self.timeEdit.time().toString() + '\n' +
                                          'Datetime : ' + self.dateTimeEdit.dateTime().toString())

a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
