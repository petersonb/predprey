

import PyQt4.QtGui as QG
import PyQt4.QtCore as QC


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

class GraphWidget(QG.QWidget):
    
    def __init__(self,size = (5.0,4.0), dpi = 100):
        super(GraphWidget, self).__init__()

        self.fig = Figure(size, dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.vbox = QG.QVBoxLayout()
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)

        self.show()

    def getFigure(self):
        return self.fig

    def draw(self):
        self.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QG.QApplication(sys.argv)
    gw = GraphWidget()

    subplot = gw.getFigure().add_subplot(111)
    subplot.plot([1,2],[1,2])
    gw.draw()
    
    sys.exit(app.exec_())
