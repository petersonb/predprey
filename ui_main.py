
from ui_central import *

import PyQt4.QtGui as QG

class MainWindow(QG.QMainWindow):
    
    def __init__(self):

        super(MainWindow,self).__init__()


        self.initUI()


    def initUI(self):
        self.central = CentralWidget()
        self.setCentralWidget(self.central)
        self.show()

if __name__ == "__main__":
    import sys
    app = QG.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
