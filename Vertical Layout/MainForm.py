from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo QVBoxLayout')

        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.button3 = QPushButton('Button 3')
        self.button4 = QPushButton('Button 4')

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)