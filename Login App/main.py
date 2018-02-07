import sys
from PyQt5.QtWidgets import QApplication

from EntryForm import *
from MainForm import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    Log = EntryForm()
    Log.show()

    a.exec()
    
