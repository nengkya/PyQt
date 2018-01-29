import sys
from PyQt5.QtWidgets import QApplication
from MainForm import *

a = QApplication(['a', 'b'])
form = MainForm()
form.show()
a.exec()
