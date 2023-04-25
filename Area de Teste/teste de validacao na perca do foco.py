from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


if __name__ == '__main__':
    app = QApplication([])
    widget = QWidget()

    button = QPushButton(widget)
    button.setGeometry(50, 50, 120, 50)
    button.setText('Clique aqui')

    button.setStyleSheet("""
        QPushButton {
            background-color: qradialgradient(cx:0.5, cy:0.5, radius: 1, fx:0.5, fy:0.5,
                stop:0 white, stop:0.7 #d2d2d2, stop: 0.8 #b9b9b9,
                stop: 0.9 #a0a0a0, stop:1 #8b8b8b);
            border-style: solid;
            border-width: 2px;
            border-color: #555555;
            border-radius: 10px;
            padding: 6px;
        }

        QPushButton:hover {
            background-color: qradialgradient(cx:0.5, cy:0.5, radius: 1, fx:0.5, fy:0.5,
                stop:0 #d4d4d4, stop:0.7 #d2d2d2, stop: 0.8 #b9b9b9,
                stop: 0.9 #a0a0a0, stop:1 #8b8b8b);
            border-color: #777777;
        }

        QPushButton:pressed {
            background-color: qradialgradient(cx:0.5, cy:0.5, radius: 1, fx:0.5, fy:0.5,
                stop:0 #a0a0a0, stop:0.7 #a2a2a2, stop: 0.8 #b9b9b9,
                stop: 0.9 #d2d2d2, stop:1 #d4d4d4);
            border-color: #555555;
        }
    """)

    widget.show()
    app.exec_()
