from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem
from Model.DAO.FuncoesAuxiliares.LimpaCampos import limpa_campos
from Model.DAO.FuncoesFormularios.VerificaDocumentoBD import verifica_documento_bd


class ClienteDAO:
    @QtCore.pyqtSlot()
    def grava_dados_cliente(self, cliente):
        msgBox = QMessageBox()
        msgBox.setText("Deseja salvar o cadastro?")
        msgBox.setWindowTitle("Confirmação")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Yes)
        buttonClicked = msgBox.exec()

        if buttonClicked == QMessageBox.Yes:
            print(cliente.tb_cli_doc)
            if verifica_documento_bd(cliente.tb_cli_doc):
                conn = ConexaoSQL
                db = conn.getConexao(ConexaoSQL)
                cursor = db.cursor()

                cursor.execute("""INSERT INTO tb_cliente(tb_cli_doc, tb_cli_nome, tb_cli_endereco, 
                                       tb_cli_numero, tb_cli_complemento, tb_cli_bairro, tb_cli_cidade, tb_cli_uf, tb_cli_cep, 
                                       tb_cli_fone_preferencial, tb_cli_fone_alternativo, tb_cli_data_nascimento, 
                                       tb_cli_contato_alternativo, tb_cli_data_cadastro, tb_cli_hora_cadastro, tb_cli_observacao) 
                                       VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
                                       '{}', '{}') """
                               .format(cliente.tb_cli_doc, cliente.tb_cli_nome,
                                       cliente.tb_cli_endereco,
                                       cliente.tb_cli_numero,
                                       cliente.tb_cli_complemento,
                                       cliente.tb_cli_bairro,
                                       cliente.tb_cli_cidade,
                                       cliente.tb_cli_uf,
                                       cliente.tb_cli_cep,
                                       cliente.tb_cli_fone_preferencial,
                                       cliente.tb_cli_fone_alternativo,
                                       cliente.tb_cli_data_nascimento,
                                       cliente.tb_cli_contato_alternativo,
                                       cliente.tb_cli_data_cadastro,
                                       cliente.tb_cli_hora_cadastro,
                                       cliente.tb_cli_observacao))
                db.commit()
                envia_mensagem('Cadastra Cliente', 'Cadastro salvo com sucesso!')
                limpa_campos(self)
            else:
                envia_mensagem('Cadastra Cliente', 'O documento informado já está cadastrado na base de dados!')
                limpa_campos(self)
                return False

        else:
            envia_mensagem('Cadastra Cliente', 'Cadastro cancelado!')
            limpa_campos(self)
            return False

    @QtCore.pyqtSlot()
    def ListaTodosClientes(self):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        sql = """SELECT tb_cli_nome FROM tb_cliente"""
        query = cursor.execute(sql)
        return query

    @QtCore.pyqtSlot()
    def LocalizaClientes(cliente):
        # if cliente.tb_cli_doc.isdigit ():
        #        print("É numero")
        # else:
        #        print("Não é numero")
        print(cliente.cad_cli_01_ob_doc, cliente.tb_cli_lista, cliente.cad_cli_03_ob_nome)
