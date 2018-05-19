import sys, PyQt5.QtWidgets, PyQt5.QtGui, PyQt5.QtCore, pdb

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(700, 300)
        self.move(300, 300)
        self.setWindowTitle('QTableWidget')

        self.table = PyQt5.QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        columnHeaders = ['Judul Buku', 'Penulis', 'Penerbit']
        self.table.setHorizontalHeaderLabels(columnHeaders)
       #self.table.setVerticalHeaderLabels(columnHeaders)

        self.addRow(0, ['PyQt5.QtWidgets.QTableWidget()', 'Dusty', 'PACKT'])
        baris = ['Assembly', 'the Art', 'Tokopedia']
        self.addRow(2, baris)
        self.addRow(3, ['a', '', ''])
        self.addRow(4)

        self.lineEdit = PyQt5.QtWidgets.QLineEdit()

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

        self.table.itemClicked.connect(self.tableItem)

    def tableItem(self):
        item = self.table.currentItem()
        self.lineEdit.setText(item.text() +
                              '[baris: %d, kolom: %d]' % (self.table.currentRow() + 1, self.table.currentColumn() + 1))

    def addRow(self, row, itemLabels = ['default', '', '']):
       #pdb.set_trace()
        for i in range (0, 3):
            item = PyQt5.QtWidgets.QTableWidgetItem()
            item.setText(itemLabels[i])
            self.table.setItem(row, i, item)

if __name__ == '__main__':
    a = PyQt5.QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
   #Enters the main event loop and waits until exit() is called, then returns the value that was set to exit()
