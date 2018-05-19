import sys, PyQt5.QtWidgets, pdb

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(700, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QTreeWidget Multi Column')

        self.tree = PyQt5.QtWidgets.QTreeWidget()
        self.tree.setColumnCount(3)
        ColumnHeaders = ['Judul', 'Penulis', 'Penerbit']
        self.tree.setHeaderLabels(ColumnHeaders)

        parent1 = self.addTopLevel('Python')
        child1  = self.addChild(parent1, 'Python OOP', 'Hasna', 'Sonny')

        self.addChild(child1, 'PyQt5', 'Hasna IT Course', 'Hasna Publisher')

        self.lineEdit = PyQt5.QtWidgets.QLineEdit('Python')
        self.lineEdit.setText('Dzakiyya')
        
        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

        self.tree.itemClicked.connect(self.treeItem)

    def treeItem(self):
        item = self.tree.currentItem()
        self.lineEdit.setText(item.text(2))

    def addTopLevel(self, category):
        item = PyQt5.QtWidgets.QTreeWidgetItem()
        item.setText(0, category)
        self.tree.addTopLevelItem(item)
        return item

    def addChild(self, parent, title, author, publisher):
        item = PyQt5.QtWidgets.QTreeWidgetItem(parent)
        item.setText(0, title)
        item.setText(1, author)
        item.setText(2, publisher)
        return item

a = PyQt5.QtWidgets.QApplication(sys.argv)

form = MainForm()
form.show()

a.exec_()
