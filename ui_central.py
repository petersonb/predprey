

import sys
import PyQt4.QtGui as QG
from ui_bottom import *
from ui_animal import *
from ui_graph import *

from predatorprey import *

class CentralWidget(QG.QWidget):
    
    def __init__(self):
        super(CentralWidget, self).__init__()

        self.buildUI()

    def buildUI(self):
        self.bottom = BottomWidget()
        self.animals = AnimalContainerWidget()
        self.animals.widgetResizable = False
        self.graph = GraphWidget()

        self.bottom.runSimButton.clicked.connect(self.graphSimulation)

        vbox = QG.QVBoxLayout()
        
        mid = QG.QHBoxLayout()
        mid.addWidget(self.graph)

        mid.addWidget(self.animals)

        vbox.addLayout(mid)

        vbox.addWidget(self.bottom)

        self.setLayout(vbox)

        self.show()

    def graphSimulation(self):
        model = PredatorPreyModel()

        animaldata = self.animals.getAnimalData()

        relationships = self.animals.getRelationshipData()
        print(relationships)
        print(animaldata)

        for d in animaldata:
            model.addAnimal(d[0],d[1],d[2])

        #r = model.addAnimal('Rabbit',50,.1)
        #f = model.addAnimal('Fox',15,-.05)
        
        for rel in relationships:
            pred = rel[0]
            predk = rel[1]
            prey = rel[2]
            preyk = rel[3]

            pd = model.getAnimalLabel(pred)
            py = model.getAnimalLabel(prey)

            model.setPredator(pd,py,predk,preyk)

        #model.setPredator(f,r,.001,.01)

        itters = self.bottom.getIterations()
        dt = self.bottom.getDeltaT()

        data = model.euler(itters,dt)

        self.graph.clear()
        self.graph.plot(data)
        self.graph.draw()


if __name__ == "__main__":
    app = QG.QApplication(sys.argv)
    cw = CentralWidget()
    sys.exit(app.exec_())
