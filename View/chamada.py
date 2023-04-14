import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Formulario(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)  # Define a geometria da janela
        self.setWindowTitle('Formulário')  # Define o título da janela

        # Cria um botão com o texto "Abrir" e conecta a função "abrir" como callback
        btn = QPushButton('Abrir', self)
        btn.move(100, 100)
        btn.clicked.connect(self.abrir)

        self.show()

    def abrir(self):
        # Aqui você pode colocar a lógica para abrir algo, como um arquivo ou uma janela
        print('Abrindo algo...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    formulario = Formulario()
    sys.exit(app.exec_())
