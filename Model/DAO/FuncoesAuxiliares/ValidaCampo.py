from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit

from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem
from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ConsultaCEPCorreio import consulta_cep_correio


def valida_campo(self, event, click):
    if isinstance(event, QKeyEvent):
        if event.key() not in [Qt.Key_Enter, Qt.Key_Return]:
            return

    current_widget = self.focusWidget()
    if not isinstance(current_widget, (QLineEdit, QComboBox, QPlainTextEdit)):
        return
    widget_name = current_widget.objectName()

    if isinstance(current_widget, QLineEdit):
        widget_text = current_widget.text()

    elif isinstance(current_widget, QComboBox):
        widget_text = current_widget.currentText()

    if 'cep' in widget_name:
        widget_cep = self.findChild(QLineEdit, widget_name)
        for combo_box in self.findChildren(QComboBox):
            if 'UF' in combo_box.objectName():
                widget_uf = combo_box
        logradouro, bairro, localidade, uf = consulta_cep_correio(widget_text)
        for widget in self.findChildren(QLineEdit):
            if 'end' in widget.objectName():
                widget.setText(logradouro)
            elif 'bairro' in widget.objectName():
                widget.setText(bairro)
            elif 'cidade' in widget.objectName():
                widget.setText(localidade)
            elif 'UF' in widget_uf.objectName():
                for i in range(widget_uf.count()):
                    if widget_uf.itemText(i) == uf:
                        widget_uf.setCurrentIndex(i)
        if logradouro == '':
            self.focusWidget()
            widget_cep.setText('')
        else:
            self.focusNextChild()
        widget_name = widget_cep.objectName()

    elif 'doc' in widget_name:
        if valida_cpf(widget_text):
            self.focusNextChild()
        else:
            envia_mensagem("Erro de validação", "CPF inválido, tente novamente por favor.")
            current_widget.setText('')

    elif 'nasc' in widget_name:
        if valida_data(widget_text):
            self.focusNextChild()
        else:
            envia_mensagem("Erro de validação", "Data inválida, tente novamente por favor.")
            current_widget.setText('')

    elif 'ob' in widget_name:
        if widget_text != '':
            self.focusNextChild()
        else:
            envia_mensagem("Erro de validação", "Esse campo é obrigatório, preencha por favor.")
            current_widget.setText('')

    elif 'ob' not in widget_name:
        self.focusNextChild()
