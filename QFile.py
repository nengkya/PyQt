import sys, PyQt5.QtWidgets, PyQt5.QtCore, PyQt5.QtGui

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(700, 300)
        self.move(300, 300)
        self.setWindowTitle('QFile dan QTextStream')

        self.label1      = PyQt5.QtWidgets.QLabel()
        self.label1.setText('Nama file')
        self.fileEdit    = PyQt5.QtWidgets.QLineEdit()
        self.fileEdit.setText('contoh.txt')
        self.label2      = PyQt5.QtWidgets.QLabel('Data yang akan ditulis')
        self.inputText   = PyQt5.QtWidgets.QTextEdit()
        self.label3      = PyQt5.QtWidgets.QLabel('Data yang dibaca')
        self.outputText  = PyQt5.QtWidgets.QTextEdit()
        self.writeButton = PyQt5.QtWidgets.QPushButton()
        self.writeButton.setText('&Write')
        self.readButton  = PyQt5.QtWidgets.QPushButton('&Read')
        hbox             = PyQt5.QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.writeButton)
        hbox.addWidget(self.readButton)
        
        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.fileEdit)
        layout.addWidget(self.label2)
        layout.addWidget(self.inputText)
        layout.addWidget(self.label3)
        layout.addWidget(self.outputText)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.writeButton.clicked.connect(self.write)
        self.readButton.clicked.connect(self.read)

    def read(self):
        f = PyQt5.QtCore.QFile(self.fileEdit.text())
        if not f.open(PyQt5.QtCore.QIODevice.ReadOnly):
            return
        self.outputText.document().setPlainText(''.join(f.readAll()))
        f.close

    def write(self):
        if len(self.fileEdit.text()) == 0:
            PyQt5.QtWidgets.QMessageBox.critical(self, 'Error', 'Nama file harus diisi.')
            return
        if self.inputText.document().isEmpty():
            PyQt5.QtWidgets.QMessageBox.critical(self, 'Error', 'Data kosong')
            return
        f = PyQt5.QtCore.QFile(self.fileEdit.text())
        if not f.open(PyQt5.QtCore.QIODevice.WriteOnly):
       #if not f.open(PyQt5.QtCore.QIODevice.WriteOnly | PyQt5.QtCore.QIODevice.Text):
       #if not f.open(PyQt5.QtCore.QIODevice.WriteOnly, PyQt5.QtCore.QIODevice.Text): koma error
            return
        inputStream = PyQt5.QtCore.QTextStream(f)
        inputStream << self.inputText.document().toPlainText()
        f.close

if __name__ == '__main__':
    a = PyQt5.QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
