import sys
from PyQt5.QtWidgets import QApplication

from MainForm import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
