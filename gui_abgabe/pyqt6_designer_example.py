import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Mandelbrot.run_video import main



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        x_pos = 0
        y_pos = 0
        # Mit progress-bar
        uic.loadUi("gui_data_progress_bar.ui", self)
        self.setMouseTracking(True)
        # Ohne progress-bar
        # uic.loadUi("gui_data.ui", self)

        # Widgets from MainWIndow
        # Wenn der 'pushButton' geklickt wird
        self.pushButton.clicked.connect(self.handleButtonClick)
        self.setWindowTitle("Mandelbrot Zoom")
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon

        # External windows
        self.dialogWindow = DialogWindow()
        self.dialogWindow.pushButton.clicked.connect(self.dialogWindow.close)
        self.show()

        # load the Picture into the Graphicsview
        self.label = QGraphicsView(self)
        pix = QPixmap('Icon.jpg')
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        # zoom_faktor
        self.zoom_faktor_einstellen.setValue(1.2)
        self.zoom_faktor_einstellen.setMaximum(4)
        self.zoom_faktor_einstellen.setMinimum(1.2)
        self.zoom_faktor_einstellen.setSingleStep(0.1)
        value_zoom = self.zoom_faktor_einstellen.value()
        print(value_zoom)

        # tooltips
        self.zoom_faktor_einstellen.setToolTip('Zoomfaktor einstellen')
        self.pushButton.setToolTip('reseet des Zommfaktor')
        self.graphicsView.setToolTip('Bild des Mandelbrot')
        self.progressBar.setToolTip('Fortschritt der Berechnung')

    def mouseMoveEvent(self, event):
        mouseEvent = event[0]
        mousePoint = mouseEvent.pos()

        if p.p1.sceneBoundingRect().contains(mousePoint):
            print('x=', mousePoint.x(), ' y=', mousePoint.y())

        global Mouse_X
        global Mouse_Y
        try:
            Mouse_X = event.x()
            Mouse_Y = event.y()
            print("mouse X,Y: {},{}".format(Mouse_X, Mouse_Y))
        except:
            pass

    # def mouseMoveEvent(self, event):
    #     s = event.windowPos()
    #     self.setMouseTracking(True)
    #     self.label_mouse_x.setText('X:' + str(s.x()))
    #     self.label_mouse_y.setText('Y:' + str(s.y()))
    #     # print("mouse X,Y: {},{}".format(Mouse_X, Mouse_Y))

    def handleButtonClick(self):
        self.dialogWindow.show()
        # hoi du


class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon
        # uic.loadUi("gui_data.ui", self)

        # self.pushButton.clicked.connect(self.close)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
