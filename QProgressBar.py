import sys, PyQt5.QtWidgets

a = PyQt5.QtWidgets.QApplication(sys.argv)

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 400)
        self.move(300, 300)
        self.setWindowTitle('Demo QProgressBar')

        self.label1 = PyQt5.QtWidgets.QLabel()
        self.label1.setText('Bilangan Ganjil')
        self.list1  = PyQt5.QtWidgets.QListWidget()

        vbox1 = PyQt5.QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.list1)

        self.label2 = PyQt5.QtWidgets.QLabel()
        self.label2.setText('Bilangan Genap')
        self.list2  = PyQt5.QtWidgets.QListWidget()
        
        vbox2 = PyQt5.QtWidgets.QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.list2)

        hbox = PyQt5.QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.progress = PyQt5.QtWidgets.QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(10000)
        self.progress.setValue(0)
        self.startButton = PyQt5.QtWidgets.QPushButton()
        self.startButton.setText('&Mulai,,')

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.progress)
        layout.addWidget(self.startButton)
        self.setLayout(layout)

        self.startButton.clicked.connect(self.start)

    def start(self):
        self.progress.setValue(0)
        for i in range(0, 10000):
           #PyQt5.QtWidgets.QApplication.processEvents()
            if i % 2 == 1:
                self.list1.addItem(str(i))
            else:
                self.list2.addItem(str(i))
            self.progress.setValue(self.progress.value() + 1)

form = MainForm()
form.show()

a.exec_()
