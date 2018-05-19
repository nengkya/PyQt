import sys, PyQt5 #.QtWidgets, PyQt5.QtCore

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QSlider dan QLCDNumber')
        
        self.slider = PyQt5.QtWidgets.QSlider(PyQt5.QtCore.Qt.Horizontal)
        self.slider.setMinimum(-1)
        self.slider.setMaximum(102)
        self.slider.setValue(45)

        self.lcd = PyQt5.QtWidgets.QLCDNumber()
        self.lcd.setDigitCount(4)
        self.lcd.display(13)

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lcd)
        self.setLayout(layout)

        self.slider.sliderMoved.connect(self.sliderMoved)

    def sliderMoved(self):
        self.lcd.display(self.slider.value())

a = PyQt5.QtWidgets.QApplication(sys.argv)
form = MainForm()
form.show()
a.exec_()
