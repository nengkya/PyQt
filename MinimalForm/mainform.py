import sys
from PyQt5.QtWidgets import QApplication
from form import *

if __name__ == '__main__':
    a = QApplication(sys.argv)
    minform = MinimalForm()
    minform.show()
    a.exec()
