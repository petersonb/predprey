
import PyQt4.QtGui as QG

class AnimalWidget(QG.QWidget):
    
    def __init__(self, name, growthk, initialPop):
        super(AnimalWidget, self).__init__()
        

        self.nameEdit = QG.QLineEdit(str(name))
        self.growthEdit = QG.QLineEdit(str(growthk))
        self.popEdit = QG.QLineEdit(str(initialPop))

        nameLabel = QG.QLabel('Animal: ')
        growthLabel = QG.QLabel('Growth: ')
        popLabel = QG.QLabel('Initial P: ')

        grid = QG.QGridLayout()
        
        grid.addWidget(nameLabel,0,0)
        grid.addWidget(self.nameEdit,0,1)
        grid.addWidget(popLabel,1,0)
        grid.addWidget(self.popEdit,1,1)
        grid.addWidget(growthLabel,2,0)
        grid.addWidget(self.growthEdit,2,1)

        self.setLayout(grid)

        self.show()

    def remove(self):
        self.destroy()
        self.close()

    def getData(self):
        return (self.nameEdit.text(),int(self.popEdit.text()),float(self.growthEdit.text()))

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
        
        self.setFixedWidth(200)

        self.show()

    def addAnimal(self):
        new = AnimalWidget('name',0,1)
        self.animals.append(new)
        self.animalLayout.addWidget(new)

    def destroyAnimal(self):
        if len(self.animals) > 1:
            animal = self.animals[-1]
            animal.remove()
            animal.destroy()
            self.animals = self.animals[:-1]

    def getAnimalData(self):
        data = []
        for animal in self.animals:
            data.append(animal.getData())
        return data

if __name__ == "__main__":
    import sys
    app = QG.QApplication(sys.argv)
    a = AnimalContainerWidget()
    sys.exit(app.exec_())
        
