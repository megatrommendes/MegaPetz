from PyQt5.QtWidgets import QLineEdit
from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ConsultaCEPCorreio import consulta_cep_correio
from Model.DAO.FuncoesAuxiliares.ValidaTelefone import valida_telefone


def botao_salvar_cliente(self):
    widgets = sorted(self.findChildren(QLineEdit), key=lambda w: w.objectName())
    i = 0
    ok = True  # variável que será retornada no final
    while i < len(widgets):  # enquanto houver widgets a serem verificados
        nome_widget = str(widgets[i].objectName())

        if ('doc' in nome_widget) and (
                valida_cpf(widgets[i].text()) is False):  # se o nome do widget contém 'doc'
            widgets[i].setFocus()
            widgets[i].setText('')
            ok = False
            break

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
                # self.ui.cad_cli_08_ob_estado.setCurrentText(uf)

        if ('ob' in nome_widget) and (widgets[i].text().strip() == ''):  # se o nome do widget contém 'ob'
            widgets[i].setFocus()
            ok = False
            break

        i += 1  # avançar para o próximo widget

    return ok



'''   
    nome = self.ui.cad_cli_03_ob_nome.text()
    end = self.ui.cad_cli_05_ob_end.text()
    end_numero = self.ui.cad_cli_06_ob_num.text()
    complemento = self.ui.cad_cli_07_complemento.text()
    UF = str(self.ui.cad_cli_08_UF.currentText())
    bairro = self.ui.cad_cli_09_ob_bairro.text()
    cidade = self.ui.cad_cli_10_ob_cidade.text()
    cep = self.ui.cad_cli_04_ob_cep.text()
    fone_preferencial = self.ui.cad_cli_11_ob_fone_pref.text()
    fone_alternativo = self.ui.cad_cli_12_fone_alt.text()
    data_nascimento = self.ui.cad_cli_02_ob_nasc.text()
    contato_alternativo = self.ui.cad_cli_13_contato.text()
    data_cadastro = datetime.now().strftime('%d/%m/%Y')
    hora_cadastro = datetime.now().strftime('%H:%Mh')
    observacao = self.ui.cad_cli_14_obs.document().toPlainText()
    cliente = ClienteCTR
    
    if not cliente.CadastraCliente(documento, nome, end, end_numero, complemento, bairro, cidade,
                                   UF, cep,
                                   fone_preferencial, fone_alternativo, data_nascimento, contato_alternativo,
                                   data_cadastro, hora_cadastro, observacao):
        parent_widget = self.ui.centralwidget  # substitua pelo widget pai apropriado
        partial(limpar_campos, parent_widget)()  # usa a função partial para passar o widget pai como argumento


def limpar_campos(parent_widget):
    for child_widget in parent_widget.findChildren((QLineEdit, QPlainTextEdit)):
        if isinstance(child_widget, QLineEdit) or isinstance(child_widget, QPlainTextEdit):
            #child_widget.clear()
            child_widget.setFocus()
            print(child_widget.objectName())
'''




