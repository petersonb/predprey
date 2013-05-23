
import PyQt4.QtGui as QG
import PyQt4.QtCore as QC

class BottomWidget(QG.QWidget):
    
    def __init__(self):
        super(BottomWidget, self).__init__()

        iterLabel = QG.QLabel('Iterations: ')
        dtLabel = QG.QLabel('delta t: ')

        self.iterInput = QG.QLineEdit('1000')
        self.dtInput = QG.QLineEdit('.01')

        self.runSimButton = QG.QPushButton('Run Simulation')
        self.graphAvAButton2d = QG.QPushButton('Graph Animal vs Animal')
        self.graphAvTButton = QG.QPushButton('Graph Animals vs Time')

        ebox = QG.QHBoxLayout()
        ebox.addWidget(self.graphAvAButton2d)
        ebox.addWidget(self.graphAvTButton)
        ebox.addStretch(1)
        ebox.addWidget(iterLabel)
        ebox.addWidget(self.iterInput)
        ebox.addWidget(dtLabel)
        ebox.addWidget(self.dtInput)
        ebox.addWidget(self.runSimButton)

        self.setLayout(ebox)

        self.show()

    def getDeltaT(self):
        return float(self.dtInput.text())

    def getIterations(self):
        return int(self.iterInput.text())


if __name__ == '__main__':
    import sys
    
    app = QG.QApplication(sys.argv)
    b = BottomWidget()
    sys.exit(app.exec_())
