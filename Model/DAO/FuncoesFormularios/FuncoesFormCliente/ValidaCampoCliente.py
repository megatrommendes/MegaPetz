from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit, QLabel

from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ConsultaCEPCorreio import consulta_cep_correio
from Model.DAO.FuncoesAuxiliares.ValidaTelefone import valida_telefone
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto
from Model.DAO.FuncoesFormularios.VerificaDocumentoBD import verifica_documento_bd


def valida_campo(self, event, operacao):
    widgets_ordenados = sorted(self.findChildren((QLineEdit, QPlainTextEdit, QComboBox, QLabel)),
                               key=lambda w: w.objectName())
    todos_widgets = {widget.objectName(): widget for widget in widgets_ordenados}
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

    if 'doc' in widget_name:
        if valida_cpf(widget_text):
            # Verifica se o numero do documente existe na base de dados
            if verifica_documento_bd(todos_widgets, operacao, widget_text):

                # Operação for "A" ativa o modo de alteração do cadastro e carrega os dados do cliente no formulário
                if operacao == 'A':
                    current_widget.setEnabled(False)

                # Operação for "C" se o cadastro existe, caso exista emite mensagem, caso não libera o cadastro
                if operacao == 'C':
                    current_widget.setEnabled(False)

                # Operação for "CC" ativa o modo de consulta e exibe os dados na tela caso encontrado
                if operacao == 'CC':
                    current_widget.setText('')
            else:
                current_widget.setText('')
        else:
            current_widget.setText('')

    elif 'nasc' in widget_name:
        if valida_data(self, widget_text):
            self.focusNextChild()
        else:
            current_widget.setText('')

    elif 'fone_pref' in widget_name:
        if valida_telefone(widget_text) is True:
            self.focusNextChild()
        else:
            current_widget.setText('')

    elif 'fone_alt' in widget_name:
        if widget_text != '':
            if valida_telefone(widget_text) is True:
                self.focusNextChild()
            else:
                current_widget.setText('')
        else:
            self.focusNextChild()

    elif 'cep' in widget_name:
        widget_cep = self.findChild(QLineEdit, widget_name)
        for combo_box in self.findChildren(QComboBox):
            if 'UF' in combo_box.objectName():
                widget_uf = combo_box
        logradouro, bairro, localidade, uf, validacao = consulta_cep_correio(widget_text)
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
            self.focusNextChild()
        widget_name = widget_cep.objectName()

    elif 'ob' in widget_name:
        if valida_texto(widget_text) is True:
            self.focusNextChild()
        else:
            current_widget.setText('')

    elif 'ob' not in widget_name:
        self.focusNextChild()
