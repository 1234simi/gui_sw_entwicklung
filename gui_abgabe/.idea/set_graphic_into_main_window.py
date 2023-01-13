from PyQt5 import QtCore, QtGui, QtWidgets

class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QtWidgets.QGraphicsScene(self)
        self.setScene(scene)
        self._pixmap_item = QtWidgets.QGraphicsPixmapItem()
        scene.addItem(self.pixmap_item)
    @property
    def pixmap_item(self):
        return self._pixmap_item

    def setPixmap(self, pixmap):
        self.pixmap_item.setPixmap(pixmap)

    def resizeEvent(self, event):
        self.fitInView(self.pixmap_item, QtCore.Qt.KeepAspectRatio)
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        if self.pixmap_item is self.itemAt(event.pos()):
            sp = self.mapToScene(event.pos())
            lp = self.pixmap_item.mapFromScene(sp).toPoint()
            print(lp)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = GraphicsView()
    w.setPixmap(QtGui.QPixmap("cat_1.png"))
    w.showMaximized()
    sys.exit(app.exec_())