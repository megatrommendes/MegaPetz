from PyQt5.QtCore import QRegExp, QEvent, Qt
from PyQt5.QtWidgets import QLineEdit
from Model.DAO.FuncoesAuxiliares.ValidaCampo import valida_campo

from PyQt5.QtGui import QKeyEvent


def botao_salvar_cliente(self):
    # Cria um evento QKeyEvent simulando a tecla Enter pressionada
    enter_event = QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier, "", False, 1)

    # Encontra o primeiro widget vazio com nome que contém 'ob' de acordo com a ordem de tabulação
    widgets = self.findChildren(QLineEdit, QRegExp('.*ob.*'))
    widgets = sorted(widgets, key=lambda x: x.objectName())
    widget = None
    for w in widgets:
        if 'ob' in w.objectName() and w.text() == '':
            widget = w
            break

        if 'ob' in w.objectName() and w.text() != '':
            widget = w
            if not valida_campo(self, enter_event):
                print('incorreto')
                widget.setFocus()

            else:
                print('correto')
    #if widget is not None:
        # Envia foco para o widget com texto em branco
        #widget.setFocus()

