import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QMessageBox

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Formulário')
        self.setGeometry(100, 100, 400, 300)

        # Criando os Labels
        label1 = QLabel('Nome:', self)
        label2 = QLabel('Idade:', self)
        label3 = QLabel('Telefone:', self)
        label4 = QLabel('Email:', self)
        label5 = QLabel('Endereço:', self)

        # Criando os Line Edits
        self.line_edits = []
        for i in range(5):
            self.line_edits.append(QLineEdit(self))

        # Conectando o sinal editingFinished() dos Line Edits ao método verificar_campo_vazio()
        for line_edit in self.line_edits:
            line_edit.editingFinished.connect(self.verificar_campo_vazio)

        # Criando o Layout
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(self.line_edits[0])
        vbox.addWidget(label2)
        vbox.addWidget(self.line_edits[1])
        vbox.addWidget(label3)
        vbox.addWidget(self.line_edits[2])
        vbox.addWidget(label4)
        vbox.addWidget(self.line_edits[3])
        vbox.addWidget(label5)
        vbox.addWidget(self.line_edits[4])

        self.setLayout(vbox)
        self.show()

    for line_edit in self.line_edits:
        line_edit.focusOutEvent.connect(self.verificar_campo_vazio)

    def verificar_campo_vazio(self):
        line_edit = self.sender()
        if line_edit.text() == '':
            QMessageBox.critical(self, 'Erro', 'Por favor, preencha todos os campos.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Formulario()
    sys.exit(app.exec_())

