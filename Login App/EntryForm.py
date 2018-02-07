import sys
from PyQt5.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication

class EntryForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(320, 280)
        self.setWindowTitle('Login App')

        okButton     = QPushButton('OK')
        cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        self.LoginLabel    = QLabel('Login')
        self.LoginLine     = QLineEdit()
        self.PasswordLabel = QLabel('Password')
        self.PasswordLine  = QLineEdit()
        
        layout = QGridLayout()
        layout.addWidget(self.LoginLabel,    0, 0)
        layout.addWidget(self.LoginLine,     0, 1)
        layout.addWidget(self.PasswordLabel, 1, 0)
        layout.addWidget(self.PasswordLine,  1, 1)
        
        layout.addLayout(hbox, 2, 1)
        self.setLayout(layout)
        
        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    login = EntryForm()
    login.exec()

    #form = MainForm()
    #form.show()

    a.exec_()
