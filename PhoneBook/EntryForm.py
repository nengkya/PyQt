from PyQt5.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class EntryForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(320, 280)
        self.setWindowTitle('Tambah/Ubah Kontak')

        self.okButton     = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        self.label1 = QLabel('Nama Lengkap :')
        nameLineEdit  = QLineEdit()
        self.label2 = QLabel('NOmor HP :')
        phoneLineEdit = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(nameLineEdit,  0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(phoneLineEdit, 1, 1)
        
        layout.addLayout(hbox, 2, 1)
        self.setLayout(layout)
        
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = EntryForm()
    form.show()
    a.exec()
