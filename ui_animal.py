
import PyQt4.QtGui as QG

class AnimalWidget(QG.QWidget):
    
    def __init__(self, name, growthk):
        super(AnimalWidget, self).__init__()
        

        self.nameEdit = QG.QLineEdit(str(name))
        self.growthEdit = QG.QLineEdit(str(growthk))

        nameLabel = QG.QLabel('Animal')
        growthLabel = QG.QLabel('growth : ')

        grid = QG.QGridLayout()
        
        grid.addWidget(nameLabel,0,0)
        grid.addWidget(self.nameEdit,0,1)
        grid.addWidget(growthLabel,1,0)
        grid.addWidget(self.growthEdit,1,1)

        self.setLayout(grid)

        self.show()

    def remove(self):
        self.destroy()
        self.close()

class AnimalContainerWidget(QG.QWidget):
    
    def __init__(self):
        super(AnimalContainerWidget, self).__init__()

        self.animals = []

        addButton = QG.QPushButton('Add Animal')
        addButton.clicked.connect(self.addAnimal)

        delButton = QG.QPushButton('Delete Animal')
        delButton.clicked.connect(self.destroyAnimal)


        self.animalLayout = QG.QVBoxLayout()
        vlayout = QG.QVBoxLayout()

        vlayout.addLayout(self.animalLayout)
        vlayout.addStretch(1)
        vlayout.addWidget(addButton)
        vlayout.addWidget(delButton)

        self.setLayout(vlayout)

        self.addAnimal()

        self.show()

    def addAnimal(self):
        new = AnimalWidget('name','growth')
        self.animals.append(new)
        self.animalLayout.addWidget(new)

    def destroyAnimal(self):
        if len(self.animals) > 1:
            animal = self.animals[-1]
            animal.remove()
            animal.destroy()
            self.animals = self.animals[:-1]


if __name__ == "__main__":
    import sys
    app = QG.QApplication(sys.argv)
    a = AnimalContainerWidget()
    sys.exit(app.exec_())
        
