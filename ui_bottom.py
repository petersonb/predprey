
import PyQt4.QtGui as QG
import PyQt4.QtCore as QC

class BottomWidget(QG.QWidget):
    
    def __init__(self):
        super(BottomWidget, self).__init__()

        iterLabel = QG.QLabel('Iterations: ')
        dtLabel = QG.QLabel('delta t: ')

        iterInput = QG.QLineEdit('1000')
        dtInput = QG.QLineEdit('.01')

        runSimButton = QG.QPushButton('Run Simulation')

        ebox = QG.QHBoxLayout()
        ebox.addStretch(1)
        ebox.addWidget(iterLabel)
        ebox.addWidget(iterInput)
        ebox.addWidget(dtLabel)
        ebox.addWidget(dtInput)
        ebox.addWidget(runSimButton)

        self.setLayout(ebox)

        self.show()


if __name__ == '__main__':
    import sys
    
    app = QG.QApplication(sys.argv)
    b = BottomWidget()
    sys.exit(app.exec_())
