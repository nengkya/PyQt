import sys, PyQt5.QtWidgets

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 300)
        self.move(300, 300)
        self.setWindowTitle('PyQt standard file library')

        self.label1      = PyQt5.QtWidgets.QLabel()
        self.label1.setText('Nama file')
        self.fileEdit    = PyQt5.QtWidgets.QLineEdit()
        self.fileEdit.setText('contoh.txt')
        self.label2      = PyQt5.QtWidgets.QLabel('Data yang akan ditulis')
        self.inputText   = PyQt5.QtWidgets.QTextEdit()
        self.label3      = PyQt5.QtWidgets.QLabel('Data yang dibaca')
        self.outputText  = PyQt5.QtWidgets.QTextEdit()
       #self.outputText.setReadOnly(True)
        self.writeButton = PyQt5.QtWidgets.QPushButton()
        self.writeButton.setText('&Ok')
        self.readButton  = PyQt5.QtWidgets.QPushButton('&Read')

        hbox = PyQt5.QtWidgets.QHBoxLayout()
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
        f = open(self.fileEdit.text(), 'r')
        self.outputText.document().setPlainText('awal'.join(f.readlines()))
        f.close

    def write(self):
        if len(self.fileEdit.text()) == 0:
       #if len(self.fileEdit.text().strip()) == 0:
            PyQt5.QtWidgets.QMessageBox.critical(self, 'Kesalahan', 'Nama file harus diisi')
            return
        if self.inputText.document().isEmpty():
            PyQt5.QtWidgets.QMessageBox.critical(self, '', 'Data yang akan ditulis harus diisi') #argumen parameter minimal 3
            return
        f = open(self.fileEdit.text(), 'w')
        f.writelines(self.inputText.document().toPlainText())
        f.close

if __name__ == '__main__':
    a = PyQt5.QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
