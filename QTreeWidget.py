import sys, PyQt5.QtWidgets

class MainForm(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QTreeWidget')
        
        self.tree = PyQt5.QtWidgets.QTreeWidget()
        
        parent1 = self.addTopLevel('Induk 1')
       #parent1 = PyQt5.QtWidgets.QTreeWidgetItem('Induk 1')
        
        child1  = self.addChild(parent1, 'Anak 1-1')
        self.addChild(child1, 'Cucu 1-1-1')
        self.addChild(child1, 'Cucu 1-1-2')

        self.addChild(parent1, 'Anak 1-2')
        self.addChild(parent1, 'Anak 1-3')

        self.lineEdit = PyQt5.QtWidgets.QLineEdit('Hasna')
       #self.lineEdit.setText('Dzakiyya')

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

        self.tree.itemClicked.connect(self.treeItem)
 
    def addTopLevel(self, itemText):
        item = PyQt5.QtWidgets.QTreeWidgetItem()
        item.setText(0, itemText) #column 0
        self.tree.addTopLevelItem(item)
        return item

    def addChild(self, parent, itemText):
        item = PyQt5.QtWidgets.QTreeWidgetItem()
        item.setText(0, itemText)
        parent.addChild(item)
        return item

    def treeItem(self):
        item = self.tree.currentItem()
        self.lineEdit.setText(item.text(0)) #column 0

a = PyQt5.QtWidgets.QApplication(sys.argv)

form = MainForm()
form.show()

a.exec_()
