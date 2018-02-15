from PyQt5 import QtWidgets
import sys

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QCalendarWidget')

        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.setGridVisible(True) #garis kota tiap tanggal
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.LongDayNames)

        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')

        shortNameCheck = QtWidgets.QCheckBox()
        shortNameCheck.setText('&Nama hari pendek')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(shortNameCheck)
        layout.addWidget(self.dateEdit)
        self.setLayout(layout)

a = QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec()
