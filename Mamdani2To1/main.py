import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


#load both ui file
uifile_1 = 'UI/halutama.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'UI/varpage.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Example(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.btnNew.clicked.connect(self.change)

    def change(self):
        self.main = MainPage()
        self.main.show()
        self.close()

class MainPage(base_2, form_2):
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,0,0.25,0.5,0.75,1,1])
        widget = QtGui.QWidget(self)
        layout = QtGui.QHBoxLayout(widget)
        layout.addWidget(sc)
        layout.addWidget(self.tableWidget)
        self.setCentralWidget(widget)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())