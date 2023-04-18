from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


def botao_salvar_cliente(self, event, click):
    if click == Qt.LeftButton:
        # Encontra o primeiro widget vazio com nome que contém '0' de acordo com a ordem de tabulação
        widgets = self.findChildren(QLineEdit, QRegExp('.*0.*'))
        widget = None
        for w in widgets:
            if '0' in w.objectName() and w.text() == '':
                widget = w
                break
        if widget is not None:
            # Exibe mensagem de erro
            envia_mensagem("Erro", "Por favor, preencha todos os campos antes de salvar.")
            # Envia foco para o widget com texto em branco
            widget.setFocus()
