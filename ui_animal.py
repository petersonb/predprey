
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

        self.relDialog = RelationshipDialog(self.animals,self)

        addButton = QG.QPushButton('Add Animal')
        addButton.clicked.connect(self.addAnimal)

        delButton = QG.QPushButton('Delete Animal')
        delButton.clicked.connect(self.destroyAnimal)

        relButton = QG.QPushButton('Manage Relationships')
        relButton.clicked.connect(self.manageRelationships)

        self.animalLayout = QG.QVBoxLayout()
        vlayout = QG.QVBoxLayout()

        vlayout.addLayout(self.animalLayout)
        vlayout.addStretch(1)
        vlayout.addWidget(addButton)
        vlayout.addWidget(delButton)
        vlayout.addWidget(relButton)

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

    def manageRelationships(self):
        result = self.relDialog.exec_()

    def getRelationshipData(self):
        return self.relDialog.getRelationshipData()

class RelationshipDialog(QG.QDialog):
    def __init__(self,animals,parent = None):
        super(RelationshipDialog,self).__init__()
        self.relationships = []
        self.animals = animals

        vbox = QG.QVBoxLayout()

        self.relContainer = QG.QGridLayout()

        addButton = QG.QPushButton('Add',self)
        addButton.clicked.connect(self.addRelationship)

        delButton = QG.QPushButton('Delete',self)
        delButton.clicked.connect(self.delRelationship)

        vbox.addLayout(self.relContainer)
        vbox.addStretch(1)
        vbox.addWidget(addButton)
        vbox.addWidget(delButton)
        self.setLayout(vbox)

        self.resize(500,300)

    def addRelationship(self):
        new = RelationshipWidget(self.animals)
        self.relationships.append(new)
        self.relContainer.addWidget(new)

    def delRelationship(self):
        if len(self.relationships) > 0:
            rel = self.relationships[-1]
            rel.remove()
            rel.destroy()
            self.relationships = self.relationships[:-1]

    def getRelationshipData(self):
        data = []
        for rel in self.relationships:
            d = rel.getData()
            data.append(d)

        return data

class RelationshipWidget(QG.QWidget):
    
    def __init__(self,animals):
        super(RelationshipWidget,self).__init__()

        animalNames = []

        for animal in animals:
            data = animal.getData()
            animalNames.append(data[0])

        self.predSel = QG.QComboBox()
        self.predk = QG.QLineEdit('1')
        self.preySel = QG.QComboBox()
        self.preyk = QG.QLineEdit('1')

        for a in animalNames:
            self.predSel.addItem(a)
            self.preySel.addItem(a)

        hbox = QG.QHBoxLayout()
        hbox.addWidget(self.predSel)
        hbox.addWidget(self.predk)
        hbox.addWidget(self.preySel)
        hbox.addWidget(self.preyk)

        self.setLayout(hbox)

    def getData(self):
        return (self.predSel.currentText(),float(self.predk.text()),self.preySel.currentText(),float(self.preyk.text()))

    def remove(self):
        self.close()
        self.destroy()

        
if __name__ == "__main__":
    import sys
    app = QG.QApplication(sys.argv)
    a = AnimalContainerWidget()
    sys.exit(app.exec_())
        
