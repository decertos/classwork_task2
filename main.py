import sys


from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import QPointF
from PyQt6 import uic


from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.createButton.clicked.connect(self.draw_an_ellipse)
        self.qp = QPainter()
        self.flag = False

    def draw_event(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(244, 234, 78))
            radius = randint(1, min(self.geometry().width(), self.geometry().height()))
            self.qp.drawEllipse(QPointF(randint(1, self.geometry().width()),
                                        randint(1, self.geometry().height())), radius, radius)
            self.qp.end()

    def draw_an_ellipse(self):
        self.draw_event()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())