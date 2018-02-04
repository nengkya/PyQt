import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

a = QApplication(sys.argv)

form = QWidget()
form.resize(1000, 1000)
form.move(100, 100)
form.show()
