import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.dockarea import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import numpy as np


def on_click(event):
    mouseEvent = event[0]
    mousePoint = mouseEvent.pos()
    # if mouseEvent.double():
    #     print("Double click")
    if p.p1.sceneBoundingRect().contains(mousePoint):
        print('x=', mousePoint.x(), ' y=', mousePoint.y())


class Plotter():
    def __init__(self):
        # Hintergrundfarbe
        pg.setConfigOption('background', 'white')
        # Foreground hier das koordinatensystem
        pg.setConfigOption('foreground', 'grey')

        # Das window wird created
        self.win = pg.GraphicsLayoutWidget(show=True)

        # Windows size default
        self.win.resize(1000, 500)

        # titel
        self.win.setWindowTitle('pyqtgraph example: dockarea')

        self.p1 = self.win.addPlot(title='SPECTRUM')
        self.win.show()


# Class wird initialisiert
p = Plotter()

proxy = pg.SignalProxy(p.win.scene().sigMouseClicked, rateLimit=60, slot=on_click)

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QGuiApplication.instance().exec_()