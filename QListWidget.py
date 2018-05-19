import sys, PyQt5.QtWidgets #PyQt5.QtGui #PyQt5.QtCore
#PyQt5 nama folder package, QtWidgets nama file class .so shared object C

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QListWidget')

        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText('&Elemen baru')

        self.itemEdit = PyQt5.QtWidgets.QLineEdit()
        self.label.setBuddy(self.itemEdit)

        self.addItemButton = PyQt5.QtWidgets.QPushButton()
        self.addItemButton.setText('&Tambah')

        hbox1 = PyQt5.QtWidgets.QHBoxLayout()
        hbox1.addWidget(self.itemEdit)
        hbox1.addWidget(self.addItemButton)
        hbox1.addStretch()

        vbox1 = PyQt5.QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.label)
        vbox1.addLayout(hbox1)

        self.list1 = PyQt5.QtWidgets.QListWidget()
        self.moveRightButton    = PyQt5.QtWidgets.QPushButton()
        self.moveRightButton.setText('>')
        self.moveRightAllButton = PyQt5.QtWidgets.QPushButton('&>>')
        self.moveLeftButton     = PyQt5.QtWidgets.QPushButton('<')
        self.moveLeftAllButton  = PyQt5.QtWidgets.QPushButton('&<<')

        vbox2 = PyQt5.QtWidgets.QVBoxLayout()
        vbox2.addWidget(self.moveRightButton)
        vbox2.addWidget(self.moveRightAllButton)
        vbox2.addWidget(self.moveLeftButton)
        vbox2.addWidget(self.moveLeftAllButton)
        vbox2.addStretch()
        self.list2 = PyQt5.QtWidgets.QListWidget()

        hbox2 = PyQt5.QtWidgets.QHBoxLayout()
        hbox2.addWidget(self.list1)
        hbox2.addLayout(vbox2)
        hbox2.addWidget(self.list2)

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addLayout(vbox1)
        layout.addLayout(hbox2)
        self.setLayout(layout)

        self.addItemButton.clicked.connect(self.addItem)
        self.moveRightButton.clicked.connect(self.moveRight)
        self.moveRightAllButton.clicked.connect(self.moveRightAll)
        self.moveLeftButton.clicked.connect(self.moveLeft)
        self.moveLeftAllButton.clicked.connect(self.moveLeftAll)

    def addItem(self):
       #if len(self.itemEdit.text()) == 0:
        if self.itemEdit.text() == '':
            return
        item = self.itemEdit.text()
        self.list1.addItem(item)
        self.itemEdit.clear()
        self.itemEdit.setFocus()

    def moveRight(self):
        if self.list1.currentRow() < 0:
            return
        self.list2.addItem(self.list1.currentItem().text())
        self.list1.takeItem(self.list1.currentRow())

    def moveRightAll(self):
        for index in range(self.list1.count()):
            self.list2.addItem(self.list1.item(index).text())
        self.list1.clear()

    def moveLeft(self):
        if self.list2.currentRow() < 0:
            return
        self.list1.addItem(self.list2.currentItem().text())
        self.list2.takeItem(self.list2.currentRow())

    def moveLeftAll(self):
        for index in range(self.list2.count()):
            self.list1.addItem(self.list2.item(index).text())
        self.list2.clear()

a = PyQt5.QtWidgets.QApplication(sys.argv)

form = MainForm()
form.show()

a.exec_() #buat exit program
