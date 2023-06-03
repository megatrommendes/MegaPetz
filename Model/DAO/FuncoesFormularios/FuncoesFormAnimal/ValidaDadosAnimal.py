from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit, QComboBox, QCheckBox

from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto


# Valida os dados do cliente antes de enviar para serem gravados no Banco de Dados
def valida_dados_animal(self, operacao):
    widgets_ordenados = sorted(self.findChildren((QLineEdit, QPlainTextEdit, QComboBox, QCheckBox)),
                               key=lambda w: w.objectName())
    todos_widgets = {widget.objectName(): widget for widget in widgets_ordenados}
    i = 0
    ok = True  # variável que será retornada no final informando se a validação foi bem sucedida
    documento = ''  # variável que armazena o número do documento do cliente e envia para verificação no BD

    while i < len(widgets_ordenados):  # enquanto houver widgets a serem verificados
        nome_widget = str(widgets_ordenados[i].objectName())

        if ('nasc' in nome_widget) and (
                valida_data(self, widgets_ordenados[i].text()) is False):  # se o nome do widget contém 'nasc'
            widgets_ordenados[i].setFocus()
            widgets_ordenados[i].setText('')
            ok = False
            break

        if 'ob' in nome_widget and isinstance(widgets_ordenados[i], QLineEdit):
            if valida_texto(widgets_ordenados[i].text().strip()) is False:
                widgets_ordenados[i].setFocus()
                ok = False
                break

        i += 1  # avançar para o próximo widget

    return ok, documento
