import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

a = QApplication(sys.argv)

form = QWidget()
form.resize(500, 500)
form.move(500, 100)
form.setWindowTitle('Hasna Dzakiyya')

label = QLabel('Sonny Hasna')
label.move(55, 40)
label.setParent(form)

form.show()
