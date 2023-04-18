import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Criar 5 QLineEdit e QLabel
        self.label1 = QLabel("Label 1:")
        self.l0ineedit9 = QLineEdit(objectName="l0ineEdit9")
        self.label2 = QLabel("Label 2:")
        self.lineedit2 = QLineEdit(objectName="lineEdit2")
        self.label3 = QLabel("Label 3:")
        self.l1ineedit7 = QLineEdit(objectName="l1ineEdit7")
        self.label4 = QLabel("Label 4:")
        self.lineedit4 = QLineEdit(objectName="lineEdit4")
        self.label5 = QLabel("Label 5:")
        self.lineedit5 = QLineEdit(objectName="lineEdit5")

        # Layout vertical para organizar os widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.l0ineedit9)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.lineedit2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.l1ineedit7)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.lineedit4)
        vbox.addWidget(self.label5)
        vbox.addWidget(self.lineedit5)

        # Botão para listar os QLineEdit
        btn = QPushButton("Listar QLineEdit")
        btn.clicked.connect(self.listar_lineedits)
        vbox.addWidget(btn)

        self.setLayout(vbox)

    def listar_lineedits(self):
        lineedits = [self.l0ineedit9, self.lineedit2, self.l1ineedit7, self.lineedit4, self.lineedit5]
        names = [le.objectName() for le in lineedits]
        names.sort()
        for name in names:
            print(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
