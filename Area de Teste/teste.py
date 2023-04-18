from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
import sys

class BlinkLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(0, 0, 47);")
        self._color1 = QColor(0, 0, 47)
        self._color2 = QColor(255, 145, 10)
        self._blink_count = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update_color)

    def start_blinking(self):
        self._timer.start(500)
        self.show()

    def stop_blinking(self):
        self._timer.stop()
        self.hide()

    def update_color(self):
        if self._blink_count % 2 == 0:
            self.setStyleSheet(f"background-color: {self._color2.name()};")
        else:
            self.setStyleSheet(f"background-color: {self._color1.name()};")

        self._blink_count += 1

        if self._blink_count == 6:
            self.stop_blinking()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blinking Label")
        self.setGeometry(0, 0, 200, 50)  # Define o tamanho do formulário
        self.label = BlinkLabel()
        self.setCentralWidget(self.label)
        self.label.start_blinking()
        self.center_label()

    def center_label(self):
        qr = self.label.frameGeometry()
        cp = self.frameGeometry().center()
        qr.moveCenter(cp)
        self.label.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





'''
from PyQt5.QtGui import QColor, QLinearGradient, QPainter
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5.QtWidgets import QLabel, QApplication
import sys

class GradientLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self._gradient = QLinearGradient(0, 0, 100, 0)
        self._gradient.setColorAt(0, QColor(0, 255, 0))
        self._gradient.setColorAt(1, QColor(0, 0, 0))
        self._pos = QPointF(-50, 0)
        self._direction = 1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._gradient)
        painter.setPen(Qt.NoPen)
        rect = self.rect()
        rect.setWidth(100)
        rect.moveLeft(int(self._pos.x()))
        painter.drawRect(rect)

    def update_gradient(self):
        self._pos += QPointF(5 * self._direction, 0)
        if self._pos.x() > self.width():
            self._pos.setX(self.width())
            self._direction = -1
        elif self._pos.x() < -100:
            self._pos.setX(-100)
            self._direction = 1
        self._gradient.setStart(self._pos)
        self._gradient.setFinalStop(self._pos + QPointF(100, 0))
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = GradientLabel()
    label.show()
    timer = QTimer()
    timer.timeout.connect(label.update_gradient)
    timer.start(50)
    sys.exit(app.exec_())






from PyQt5.QtGui import QColor, QLinearGradient, QPainter
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5.QtWidgets import QLabel, QApplication
import sys

class GradientLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self._gradient = QLinearGradient(0, 0, 100, 0)
        self._gradient.setColorAt(0, QColor(0, 255, 0))
        self._gradient.setColorAt(1, QColor(0, 0, 0))
        self._pos = QPointF(-50, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._gradient)
        painter.setPen(Qt.NoPen)
        rect = self.rect()
        rect.setWidth(100)
        rect.moveLeft(int(self._pos.x()))
        painter.drawRect(rect)

    def update_gradient(self):
        self._pos += QPointF(0.5, 0)
        if self._pos.x() > self.width():
            self._pos.setX(-50)
        self._gradient.setStart(self._pos)
        self._gradient.setFinalStop(self._pos + QPointF(100, 0))
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = GradientLabel()
    label.show()
    timer = QTimer()
    timer.timeout.connect(label.update_gradient)
    timer.start(10)
    sys.exit(app.exec_())




from PyQt5.QtGui import QColor, QLinearGradient, QPainter
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5.QtWidgets import QLabel, QApplication
import sys

class GradientLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self._gradient = QLinearGradient(0, 0, 100, 0)
        self._gradient.setColorAt(0, QColor(0, 255, 0))
        self._gradient.setColorAt(1, QColor(0, 0, 0))
        self._pos = QPointF(0, 0)
        self._direction = 1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

    def update_gradient(self):
        if self._direction == 1:
            self._pos += QPointF(0.01, 0)
            if self._pos.x() > self.width():
                self._direction = -1
        else:
            self._pos -= QPointF(0.01, 0)
            if self._pos.x() < 0:
                self._direction = 1
        self._gradient.setStart(self._pos)
        self._gradient.setFinalStop(self._pos + QPointF(100, 0))
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = GradientLabel()
    label.show()
    timer = QTimer()
    timer.timeout.connect(label.update_gradient)
    timer.start(1)
    sys.exit(app.exec_())


from PyQt5.QtGui import QColor, QLinearGradient, QPainter
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5.QtWidgets import QLabel, QApplication
import sys

class GradientLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self._gradient = QLinearGradient(0, 0, 100, 0)
        self._gradient.setColorAt(0, QColor(0, 255, 0))
        self._gradient.setColorAt(1, QColor(0, 0, 0))
        self._pos = QPointF(0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

    def update_gradient(self):
        self._pos += QPointF(0.01, 0)
        if self._pos.x() > self.width():
            self._pos.setX(0)
        self._gradient.setStart(self._pos)
        self._gradient.setFinalStop(self._pos + QPointF(100, 0))
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = GradientLabel()
    label.show()
    timer = QTimer()
    timer.timeout.connect(label.update_gradient)
    timer.start(1)
    sys.exit(app.exec_())



from PyQt5.QtGui import QPainter, QLinearGradient, QColor
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPoint

class GradientLabel(QLabel):
    def __init__(self, parent=None):
        super(GradientLabel, self).__init__(parent)
        self.setAutoFillBackground(True)
        self.setMinimumSize(200, 100)

        self.progress = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_gradient)
        self.timer.start(500)  # intervalo de 50 milissegundos

        self.direction = 1

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.gradient())
        painter.setPen(Qt.white)
        painter.drawText(self.rect(), Qt.AlignCenter, "Hello, World!")

    def gradient(self):
        if self.progress < 0.5:
            color1 = QColor.fromRgb(10, 10, 70)
            color2 = QColor.fromRgb(70, 70, 200)
            progress = self.progress * 2
        else:
            color1 = QColor.fromRgb(70, 70, 200)
            color2 = QColor.fromRgb(10, 10, 70)
            progress = (self.progress - 0.5) * 2
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, color1)
        gradient.setColorAt(progress, color2)
        gradient.setColorAt(1, color1)
        return gradient

    def update_gradient(self):
        if self.progress >= 1 or self.progress <= 0:
            self.direction *= -1
        self.progress += 0.01 * self.direction
        self.update()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()
    label = GradientLabel()
    layout.addWidget(label)
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())
'''