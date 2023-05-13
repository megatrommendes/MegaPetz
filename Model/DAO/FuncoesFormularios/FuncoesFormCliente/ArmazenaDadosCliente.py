from datetime import datetime

from Controller.ClienteCTR import ClienteCTR


def armazena_dados_cliente(self, documento):
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
    data_cadastro = str(datetime.now().strftime('%d/%m/%Y'))
    hora_cadastro = str(datetime.now().strftime('%H:%Mh'))
    observacao = self.ui.cad_cli_14_obs.document().toPlainText()
    cliente = ClienteCTR

    if not cliente.carrega_dados_cliente(self, documento, nome, end, end_numero, complemento, bairro, cidade,
                                         UF, cep,
                                         fone_preferencial, fone_alternativo, data_nascimento, contato_alternativo,
                                         data_cadastro, hora_cadastro, observacao):
        return False
