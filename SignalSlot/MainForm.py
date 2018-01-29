from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class MainForm(QWidget):
    def __init__(QWidget):
        super().__init__()
        QWidget.setupUi()

    def setupUi(QWidget):
        QWidget.resize(300, 100)
        QWidget.move(300, 300)
        QWidget.setWindowTitle('Demo Signal dan Slot')

        lineEdit = QLineEdit()
        lineEdit.setText('Demo Signal dan Slot')
        
        button1 = QPushButton('Bersihkan')
        button2 = QPushButton('Tutup')

        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)

        layout = QVBoxLayout()
        layout.addWidget(lineEdit)
        layout.addLayout(hbox)
        QWidget.setLayout(layout)

        button1.clicked.connect(lineEdit.clear)
        button2.clicked.connect(QWidget.close)
