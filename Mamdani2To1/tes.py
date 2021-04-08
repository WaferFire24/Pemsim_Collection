"""
import numpy as np
import matplotlib.pyplot as plt
red = [1,1,0.75,0.5,0.25,0,0]
blue = [0,0,1,1]
plt.plot(red)
plt.ylabel('some numbers')
plt.show()
"""
"""
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Using Numpy to create an array X
X = [1,2,3,4,5,6,7]

# Assign variables to the y axis part of the curve
y = [1,1,0.75,0.5,0.25,0,0]
z = [0,0,0.25,0.5,0.75,1,1]

# Plotting both the curves simultaneously
plt.plot(y, color='r', label='Turun')
plt.plot(z, color='b', label='Naik')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Angle")
plt.ylabel("Magnitude")
plt.title("Sine and Cosine functions")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
plt.xticks([])
# To load the display window
plt.show()
"""
"""
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object, 
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,0,0.25,0.5,0.75,1,1])
        self.setCentralWidget(sc)

        self.show()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
"""

"""
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys

pg.setConfigOption('background', 'w')
#pg.mkpen('b', width = 5)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('UI/mainwindow.ui', self)
        
        self.plot([0,0,0.25,0.5,0.75,1,1])
        self.plot([1,1,0.75,0.5,0.25,0,0])

    def plot(self, data):
        self.graphWidget.plot(data)
        pg.setConfigOption('foreground')

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':         
    main()
"""
"""
from PyQt5 import QtWidgets, uic
import sys
import matplotlib
matplotlib.use('Qt5Agg')
import sys
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('UI/mainwindow2.ui', self)
        
        self.plot([0,0,0.25,0.5,0.75,1,1])

    def plot(self, hour):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.graphWidget.plot([0,0,0.25,0.5,0.75,1,1])

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':         
    main()
"""
"""
import sys
from PyQt5 import QtWidgets, uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('UI/varpage.ui', self)
        self.plotWidget = plt.figure()
        self.canvas = FigureCanvas(self.plotWidget)
        self.plot_01.addWidget(self.canvas)
        self.button01.clicked.connect(self.plot)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.plotWidget.clear()

        # create an axis
        ax = self.plotWidget.add_subplot(111)
        plt.xticks([])
        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':         
    main()  
"""

"""
import sys
from PyQt5 import QtWidgets, uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.plotWidget = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.plotWidget)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.plotWidget.clear()

        # create an axis
        ax = self.plotWidget.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
"""


"""
import sys
from PyQt5.QtWidgets import *
					

#Main Window
class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 - QTableWidget'
		self.left = 0
		self.top = 0
		self.width = 300
		self.height = 200

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.createTable()

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

		#Show window
		self.show()

	#Create table
	def createTable(self):
		self.tableWidget = QTableWidget()

		#Row count
		self.tableWidget.setRowCount(4)

		#Column count
		self.tableWidget.setColumnCount(2)

		self.tableWidget.setItem(0,0, QTableWidgetItem(str(1)))
		self.tableWidget.setItem(0,1, QTableWidgetItem(str('OKEE')))
		self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
		self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
		self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
		self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal"))
		self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
		self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))

		#Table will fit the screen horizontally
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.horizontalHeader().setSectionResizeMode(
			QHeaderView.Stretch)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
"""
"""
class kelasSatu():
    def __init__(self):
        self.X = [2]
        self.tambah(self.X)
    
    def tambah(self, target):
        target.append(5)
        print(target)

if __name__ == '__main__':
    kelasSatu()
"""

"""
my_list = []

#append to the list
my_list.extend(["PYTHON", "PHP"])

#print
print(my_list)
"""

x = [1,3]

for i in x:
    print(i)