import PyQt5.QtWidgets, sys

b = PyQt5.QtWidgets.QApplication(sys.argv)

a = PyQt5.QtWidgets.QWidget()
c = PyQt5.QtWidgets.QLineEdit()
e = PyQt5.QtWidgets.QPushButton('Enter')
d = PyQt5.QtWidgets.QGridLayout()
d.addWidget(c)
d.addWidget(e)
a.setLayout(d)
a.show()

def cekPassword():
    if c.text() == 'a':
        c.setText('Password bener !')
    else:
        a.close()
        f = PyQt5.QtWidgets.QWidget()
        g = PyQt5.QtWidgets.QLabel('Password salah !')
        layout = PyQt5.QtWidgets.QGridLayout()
        layout.addWidget(g)
        f.setLayout(layout)
        f.show()

#eventSource.signal(eventTarget.slot)
e.clicked.connect(cekPassword)

b.exec()
