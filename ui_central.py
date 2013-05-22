

import sys
import PyQt4.QtGui as QG
from ui_bottom import *
from ui_animal import *

class CentralWidget(QG.QWidget):
    
    def __init__(self):
        super(CentralWidget, self).__init__()

        self.buildUI()

    def buildUI(self):
        self.bottom = BottomWidget()
        self.animals = AnimalContainerWidget()
        
        vbox = QG.QVBoxLayout()
        
        mid = QG.QHBoxLayout()
        mid.addStretch(1)
        mid.addWidget(self.animals)

        vbox.addLayout(mid)
        vbox.addStretch(1)

        vbox.addWidget(self.bottom)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    app = QG.QApplication(sys.argv)
    cw = CentralWidget()
    sys.exit(app.exec_())
