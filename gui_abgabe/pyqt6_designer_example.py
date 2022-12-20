import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtCore import *


from Mandelbrot.run_video import main

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Mit progress-bar
        uic.loadUi("gui_data_progress_bar.ui", self)
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
        pix = QPixmap('Icon.jpg')
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)




    def handleButtonClick(self):
        self.dialogWindow.show()

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