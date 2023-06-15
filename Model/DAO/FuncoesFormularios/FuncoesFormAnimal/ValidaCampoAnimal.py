from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit, QLabel, QCheckBox

from Model.DAO.FuncoesAuxiliares.CalcularDiferencaData import calcular_diferenca_data
from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto
from Model.DAO.FuncoesFormularios.VerificaDocumentoBD import verifica_documento_bd


def valida_campo_animal(self, event, operacao):
    widgets_ordenados = sorted(self.findChildren((QLineEdit, QPlainTextEdit, QComboBox, QLabel)),
                               key=lambda w: w.objectName())
    todos_widgets = {widget.objectName(): widget for widget in widgets_ordenados}
    if isinstance(event, QKeyEvent):
        if event.key() not in [Qt.Key_Enter, Qt.Key_Return]:
            return

    current_widget = self.focusWidget()
    if not isinstance(current_widget, (QLineEdit, QComboBox, QPlainTextEdit, QCheckBox)):
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
        if current_widget.text() != '':
            if valida_data(self, widget_text):
                resultado = calcular_diferenca_data(widget_text)
                idade, descricao = resultado
                self.focusNextChild()
                self.focusNextChild()
                self.focusNextChild()
                self.ui.cad_ani_04_ob_idade.setEnabled(False)
                self.ui.cad_ani_05_ob_data.setEnabled(False)
                self.ui.cad_ani_04_ob_idade.setText(str(idade))
                self.ui.cad_ani_05_ob_data.setCurrentText(descricao)
            else:
                current_widget.setText('')
                self.ui.cad_ani_04_ob_idade.setText('')
                self.ui.cad_ani_04_ob_idade.setEnabled(True)
                self.ui.cad_ani_05_ob_data.setEnabled(True)

        else:
            self.ui.cad_ani_04_ob_idade.setText('')
            self.ui.cad_ani_04_ob_idade.setEnabled(True)
            self.ui.cad_ani_05_ob_data.setEnabled(True)
            self.focusNextChild()

    elif 'ob' in widget_name:
        if valida_texto(widget_text):
            self.focusNextChild()
        else:
            if isinstance(current_widget, QLineEdit):
                current_widget.setText('')
            elif isinstance(current_widget, QComboBox):
                current_widget.setCurrentIndex(-1)

    elif 'ob' not in widget_name:
        self.focusNextChild()
