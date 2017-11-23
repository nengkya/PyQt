from PyQt5.QtWidgets import QWidget, QDesktopWidget

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300, 200)
        self.setCenter()
        self.setWindowTitle('Demo Form di Tengah Layar')

    def setCenter(self):
        desktop = QDesktopWidget()

        screenwidth  = desktop.screen().width()
        screenheight = desktop.screen().height()

        self.setGeometry( (screenwidth - self.width()) / 2,
                          (screenheight - self.height()) // 2, self.width(), self.height() )
