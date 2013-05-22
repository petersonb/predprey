

import sys
import PyQt4.QtGui as QG
from ui_bottom import *
from ui_animal import *
from ui_graph import *

class CentralWidget(QG.QWidget):
    
    def __init__(self):
        super(CentralWidget, self).__init__()

        self.buildUI()

    def buildUI(self):
        self.bottom = BottomWidget()
        self.animals = AnimalContainerWidget()
        self.graph = GraphWidget()

        fig = self.graph.getFigure().add_subplot(111)
        fig.plot([1,2],[1,2])
        
        fig2 = self.graph.getFigure().add_subplot(111)
        fig2.plot([5,7],[10,12])

        vbox = QG.QVBoxLayout()
        
        mid = QG.QHBoxLayout()
        mid.addWidget(self.graph)

        mid.addWidget(self.animals)

        vbox.addLayout(mid)

        vbox.addWidget(self.bottom)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    app = QG.QApplication(sys.argv)
    cw = CentralWidget()
    sys.exit(app.exec_())
