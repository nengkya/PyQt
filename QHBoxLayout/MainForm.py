from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(300, 100)
		self.move(300, 300)
		self.setWindowTitle('Demo QHBoxLayout')

		self.button1 = QPushButton('Button 1')
		self.button2 = QPushButton('Button 2')
		self.button3 = QPushButton('Button 3')
		self.button4 = QPushButton('Button 4')

		layout = QHBoxLayout()
		layout.addWidget(self.button1)
		layout.addWidget(self.button2)
		layout.addWidget(self.button3)
		layout.addWidget(self.button4)

		self.setLayout(layout)