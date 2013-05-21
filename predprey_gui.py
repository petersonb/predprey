
import sys
from PyQt4 import QtGui, QtCore

class PredPreyInterface(QtGui.QMainWindow):

    def __init__(self):
        super(PredPreyInterface, self).__init__()

        self.initializeInterface()

    def initializeInterface(self):

        iterlabel = QtGui.QLabel("Iterations: ")
        
        self.iterInput = QtGui.QLineEdit()
        self.iterInput.setText('1000')

        dtlabel = QtGui.QLabel("dt: ")

        self.dtinput = QtGui.QLineEdit()
        self.dtinput.setText('.01')
        

        self.runsim = QtGui.QPushButton('Run Simulation')
        self.runsim.clicked.connect(self.runSim)


        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        hbox.addWidget(iterlabel)
        hbox.addWidget(self.iterInput)
        hbox.addWidget(dtlabel)
        hbox.addWidget(self.dtinput)
        hbox.addWidget(self.runsim)


        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
    
        self.setLayout(vbox)

        self.setWindowTitle('Ecosim')
        self.show()

    def runSim(self):
        itters = self.iterInput.text()
        dt = self.dtinput.text()

        print(dt, itters)
        return itters,dt

def main():
    app = QtGui.QApplication(sys.argv)
    ppi = PredPreyInterface()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
