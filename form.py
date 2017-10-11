from PyQt5.QtWidgets import QWidget, QLabel


class MinimalForm(QWidget): #class MinimalForm turunan dari QWidget
    def __init__(self):
        super().__init__()  #init class MinimalForm from QWidget init
        self.setupUi()

    def setupUi(self):
        self.resize(200, 100)
        self.move(300, 300)
        self.setWindowTitle('GUI Minimal')

        self.label = QLabel('Hello PyQt5')
        self.label.move(55, 40)
        self.label.setParent(self)
