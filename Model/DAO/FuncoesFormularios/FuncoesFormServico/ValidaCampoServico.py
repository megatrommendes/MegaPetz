from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit, QLabel

from Model.DAO.FuncoesAuxiliares.ValidaHora import valida_hora
from Model.DAO.FuncoesAuxiliares.ValidaReal import valida_real
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto


def valida_campo_servico(self, event):
    widgets_ordenados = sorted(self.findChildren((QLineEdit, QPlainTextEdit, QLabel)),
                               key=lambda w: w.objectName())
    todos_widgets = {widget.objectName(): widget for widget in widgets_ordenados}
    if isinstance(event, QKeyEvent):
        if event.key() not in [Qt.Key_Enter, Qt.Key_Return]:
            return
    current_widget = self.focusWidget()

    if not isinstance(current_widget, (QLineEdit, QPlainTextEdit)):
        return
    widget_name = current_widget.objectName()

    if isinstance(current_widget, QLineEdit):
        widget_text = current_widget.text()

    if 'valor' in widget_name:
        if valida_real(widget_text):
            self.focusNextChild()
        else:
            if isinstance(current_widget, QLineEdit):
                current_widget.setText('')
            return

    if 'periodo' in widget_name and widget_text != '':
        if valida_hora(widget_text):
            self.focusNextChild()
        else:
            if isinstance(current_widget, QLineEdit):
                current_widget.setText('')
            return

    if 'ob' in widget_name:
        if valida_texto(widget_text):
            self.focusNextChild()
        else:
            if isinstance(current_widget, QLineEdit):
                current_widget.setText('')
            return

    elif 'ob' not in widget_name:
        self.focusNextChild()
