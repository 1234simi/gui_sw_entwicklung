# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt


class AppDemo(QMainWindow):

    def __init__(self):
        super(AppDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('666')
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('6 Shenhua Dew ')
        self.label.setGeometry(5, 5, 145, 185)
        self.label.setMouseTracking(True)

        self.label_mouse_x = QLabel(self)
        self.label_mouse_x.setGeometry(155, 5, 80, 30)
        self.label_mouse_x.setText('x')
        self.label_mouse_x.setMouseTracking(True)

        self.label_mouse_y = QLabel(self)
        self.label_mouse_y.setText('y')
        self.label_mouse_y.setGeometry(155, 40, 80, 30)
        self.label_mouse_y.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        s = event.windowPos()
        self.setMouseTracking(True)
        self.label_mouse_x.setText('X:' + str(s.x()))
        self.label_mouse_y.setText('Y:' + str(s.y()))


def run_it():
    app = QApplication(sys.argv)
    w = AppDemo()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0:256, 0:256] = [255, 0, 0]  # red patch in upper left
    print(f'shape: {data.shape}')
    img = Image.fromarray(data, 'RGB')
    # img.save('my.png')
    img.show()