

import PyQt4.QtGui as QG
import PyQt4.QtCore as QC


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

class GraphWidget(QG.QWidget):
    
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)

        self.axis = self.fig.add_subplot(111)

        #self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.vbox = QG.QVBoxLayout()
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)

        self.show()

    def getFigure(self):
        return self.fig

    def clear(self):
        self.axis.clear()

    def plot(self,data):
        x = data[0]
        ys = data[1]
        for d in ys:
            self.axis.plot(x,d)

    def plotAvA2d(self,data):
        x = data[1][0]
        y = data[1][1]
        self.axis.plot(x,y)

    def draw(self):
        self.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QG.QApplication(sys.argv)
    gw = GraphWidget()

    gw.plot([[1,2],[[1,2]]])
    gw.clear()
    gw.plot([[2,1],[[1,2]]])
    gw.draw()
    
    sys.exit(app.exec_())
