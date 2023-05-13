from PyQt5.QtWidgets import QLineEdit
from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ConsultaCEPCorreio import consulta_cep_correio
from Model.DAO.FuncoesAuxiliares.ValidaTelefone import valida_telefone
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto


def valida_dados_cliente(self):
    widgets = sorted(self.findChildren(QLineEdit), key=lambda w: w.objectName())
    i = 0
    ok = True  # variável que será retornada no final
    documento = ''

    while i < len(widgets):  # enquanto houver widgets a serem verificados
        nome_widget = str(widgets[i].objectName())

        if 'doc' in nome_widget:
            if valida_cpf(widgets[i].text()) is False:  # se o nome do widget contém 'doc'
                widgets[i].setFocus()
                widgets[i].setText('')
                ok = False
                break
            else:
                documento = widgets[i].text()

        if ('nasc' in nome_widget) and (
                valida_data(self, widgets[i].text()) is False):  # se o nome do widget contém 'nasc'
            widgets[i].setFocus()
            widgets[i].setText('')
            ok = False
            break

        if 'fone_alt' in nome_widget:
            if widgets[i].text() != '':
                if valida_telefone(widgets[i].text().strip()) is False:
                    widgets[i].setFocus()
                    widgets[i].setText('')
                    ok = False
                    break
                else:
                    widgets[i].focusNextChild()
            else:
                widgets[i].focusNextChild()

        if 'fone_pref' in nome_widget:
            if valida_telefone(widgets[i].text().strip()) is False:
                widgets[i].setFocus()
                widgets[i].setText('')
                ok = False
                break
            else:
                widgets[i].focusNextChild()

        if 'cep' in nome_widget:
            logradouro, bairro, localidade, uf, validacao = consulta_cep_correio(self.ui.cad_cli_04_ob_cep.text())
            if not validacao:
                widgets[i].clear()
                widgets[i].setFocus()
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

        if 'ob' in nome_widget:
            if valida_texto(widgets[i].text().strip()) is False:
                widgets[i].setFocus()
                ok = False
                break

        i += 1  # avançar para o próximo widget
    return ok, documento


'''   



def limpar_campos(parent_widget):
    for child_widget in parent_widget.findChildren((QLineEdit, QPlainTextEdit)):
        if isinstance(child_widget, QLineEdit) or isinstance(child_widget, QPlainTextEdit):
            #child_widget.clear()
            child_widget.setFocus()
            print(child_widget.objectName())
'''
