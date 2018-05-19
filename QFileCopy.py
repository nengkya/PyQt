import sys, PyQt5.QtWidgets

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('QFile.copy()')

        self.label1 = PyQt5.QtWidgets.QLabel()
        self.label1.setText('Nama file sumber')
        self.fileSource = PyQt5.QtWidgets.QLineEdit()
        self.fileSource.setText('contoh.txt')
        self.label2 = PyQt5.QtWidgets.QLabel('Nama file tujuan')
        self.fileDest = PyQt5.QtWidgets.QLineEdit('copyContoh.txt')
        self.copyButton = PyQt5.QtWidgets.QPushButton()
        self.copyButton.setText('&Salin file')

        hbox = PyQt5.QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.copyButton)

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.fileSource)
        layout.addWidget(self.label2)
        layout.addWidget(self.fileDest)
        layout.addLayout(hbox)
        self.setLayout(layout)

if __name__ == '__main__':
    a = PyQt5.QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
