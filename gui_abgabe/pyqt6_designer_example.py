import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from Mandelbrot.run_video import main
from gui_abgabe.probiere import GraphicsView


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
        # self.label = QGraphicsView(self)
        # self.pix = QPixmap('cat_1.png')
        # self.item = QtWidgets.QGraphicsPixmapItem(self.pix)
        # self.scene = QtWidgets.QGraphicsScene(self)
        # self.scene.addItem(self.item)
        # self.graphicsView.setScene(self.scene)


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

    def mouseDoubleClickEvent(self, event):
        """
        Gibt die Koordinaten von dem Mauszeiger zurück, wennn man Doppel-Klickt
        """
        Mouse_X = event.x()
        Mouse_Y = event.y()
        print(f'coor: {Mouse_X}, {Mouse_Y}')


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
w = GraphicsView()
w.setPixmap(QtGui.QPixmap("cat_1.png"))
app.exec()
