from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit, QComboBox

from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ConsultaCEPCorreio import consulta_cep_correio
from Model.DAO.FuncoesAuxiliares.ValidaTelefone import valida_telefone
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto
from Model.DAO.FuncoesFormularios.VerificaDocumentoBD import verifica_documento_bd


# Valida os dados do cliente antes de enviar para serem gravados no Banco de Dados
def valida_dados_cliente(self, operacao):
    widgets_ordenados = sorted(self.findChildren((QLineEdit, QPlainTextEdit, QComboBox)), key=lambda w: w.objectName())
    todos_widgets = {widget.objectName(): widget for widget in widgets_ordenados}
    i = 0
    ok = True  # variável que será retornada no final informando se a validação foi bem sucedida
    documento = ''  # variável que armazena o número do documento do cliente e envia para verificação no BD

    while i < len(widgets_ordenados):  # enquanto houver widgets a serem verificados
        nome_widget = str(widgets_ordenados[i].objectName())

        if 'doc' in nome_widget:
            if valida_cpf(widgets_ordenados[i].text()):
                if operacao == "C":
                    if verifica_documento_bd(todos_widgets, operacao, widgets_ordenados[i].text()) is False:
                        widgets_ordenados[i].setFocus()
                        widgets_ordenados[i].setText('')
                        ok = False
                        break
                    else:
                        documento = widgets_ordenados[i].text()
            else:
                widgets_ordenados[i].setFocus()
                widgets_ordenados[i].setText('')
                ok = False
                break

        if ('nasc' in nome_widget) and (
                valida_data(self, widgets_ordenados[i].text()) is False):  # se o nome do widget contém 'nasc'
            widgets_ordenados[i].setFocus()
            widgets_ordenados[i].setText('')
            ok = False
            break

        if 'fone_alt' in nome_widget:
            if widgets_ordenados[i].text() != '':
                if valida_telefone(widgets_ordenados[i].text().strip()) is False:
                    widgets_ordenados[i].setFocus()
                    widgets_ordenados[i].setText('')
                    ok = False
                    break
                else:
                    widgets_ordenados[i].focusNextChild()
            else:
                widgets_ordenados[i].focusNextChild()

        if 'fone_pref' in nome_widget:
            if valida_telefone(widgets_ordenados[i].text().strip()) is False:
                widgets_ordenados[i].setFocus()
                widgets_ordenados[i].setText('')
                ok = False
                break
            else:
                widgets_ordenados[i].focusNextChild()

        if 'cep' in nome_widget:
            logradouro, bairro, localidade, uf, validacao = consulta_cep_correio(self.ui.cad_cli_04_ob_cep.text())
            if not validacao:
                widgets_ordenados[i].clear()
                widgets_ordenados[i].setFocus()
                ok = False
                break
            else:
                # preencher campos de endereço
                self.ui.cad_cli_05_ob_end.setText(logradouro)
                self.ui.cad_cli_09_ob_bairro.setText(bairro)
                self.ui.cad_cli_10_ob_cidade.setText(localidade)
                for j in range(self.ui.cad_cli_08_UF.count()):
                    if self.ui.cad_cli_08_UF.itemText(j) == uf:
                        self.ui.cad_cli_08_UF.setCurrentIndex(j)
                        break

        if 'ob' in nome_widget and isinstance(widgets_ordenados[i], QLineEdit):
            if valida_texto(widgets_ordenados[i].text().strip()) is False:
                widgets_ordenados[i].setFocus()
                ok = False
                break

        i += 1  # avançar para o próximo widget

    return ok, documento
