from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap

from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesAuxiliares.AbilitaCampo import abilita_campo
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem
from Model.DAO.FuncoesAuxiliares.LimpaCampos import limpa_campos
from Model.DAO.FuncoesAuxiliares.ReposicionaFoco import reposiciona_foco


class ClienteDAO:
    @QtCore.pyqtSlot()
    def grava_dados_cliente(self, operacao, cliente):
        msgBox = QMessageBox()
        msgBox.setText("Deseja salvar o cadastro?")
        msgBox.setWindowTitle("Confirmação")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Yes)
        buttonClicked = msgBox.exec()

        if buttonClicked == QMessageBox.Yes:
            conn = ConexaoSQL
            db = conn.getConexao(ConexaoSQL)
            cursor = db.cursor()

            if operacao == 'C':
                query = """INSERT INTO tb_cliente(tb_cli_doc, tb_cli_nome, tb_cli_endereco, 
                           tb_cli_numero, tb_cli_complemento, tb_cli_bairro, tb_cli_cidade, tb_cli_uf, tb_cli_cep, 
                           tb_cli_fone_preferencial, tb_cli_fone_alternativo, tb_cli_data_nascimento, 
                           tb_cli_contato_alternativo, tb_cli_data_cadastro, tb_cli_hora_cadastro, tb_cli_observacao) 
                           VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
                           '{}', '{}') """

                cursor.execute(query.format(cliente.tb_cli_doc, cliente.tb_cli_nome,
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
                pixmapFrontal = QPixmap(self.ui.imagemcamera_frontal_label.pixmap())
                pixmapVerso = QPixmap(self.ui.imagemcamera_tras_label.pixmap())
                caminhoFrontal = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(cliente.tb_cli_doc + '-FRENTE')
                caminhoVerso = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(cliente.tb_cli_doc + '-VERSO')

                # Salva a imagem no arquivo
                pixmapFrontal.save(caminhoFrontal)
                pixmapVerso.save(caminhoVerso)
                envia_mensagem('Cadastra Cliente', 'Cadastro salvo com sucesso!')

            elif operacao == 'A':
                query = """UPDATE tb_cliente SET tb_cli_nome = '{}', tb_cli_endereco = '{}', tb_cli_numero 
                           = '{}', tb_cli_complemento = '{}', tb_cli_bairro = '{}', tb_cli_cidade = '{}', tb_cli_uf = '{}', 
                           tb_cli_cep = '{}', tb_cli_fone_preferencial = '{}', tb_cli_fone_alternativo = '{}', 
                           tb_cli_data_nascimento = '{}', tb_cli_contato_alternativo = '{}', tb_cli_observacao = '{}' WHERE 
                           tb_cli_doc = '{}' """

                cursor.execute(query.format(cliente.tb_cli_nome,
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
                                            cliente.tb_cli_observacao,
                                            cliente.tb_cli_doc))

                db.commit()

                pixmapFrontal = QPixmap(self.ui.imagemcamera_frontal_label.pixmap())
                pixmapVerso = QPixmap(self.ui.imagemcamera_tras_label.pixmap())
                caminhoFrontal = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(cliente.tb_cli_doc + '-FRENTE')
                caminhoVerso = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(cliente.tb_cli_doc + '-VERSO')

                # Salva a imagem no arquivo
                pixmapFrontal.save(caminhoFrontal)
                pixmapVerso.save(caminhoVerso)
                envia_mensagem('Altera Cliente', 'Cadastro alterado com sucesso!')

            limpa_campos(self)
            abilita_campo(self)
            reposiciona_foco(self)
            pixmap = QPixmap('C:\\MegaPetz\\imagens\\imagem_icones\\icons-câmera.png')
            QPixmap(self.ui.imagemcamera_frontal_label.setPixmap(pixmap))
            QPixmap(self.ui.imagemcamera_tras_label.setPixmap(pixmap))
        else:
            if operacao == 'C':
                envia_mensagem('Cadastra Cliente', 'Cadastro cancelado!')
            elif operacao == 'A':
                envia_mensagem('Altera Cliente', 'Alteração cancelada!')

            limpa_campos(self)
            abilita_campo(self)
            reposiciona_foco(self)

        return False

    @QtCore.pyqtSlot()
    def carrega_cliente(self):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        sql = """SELECT * FROM tb_cliente"""
        cursor.execute(sql)
        resultados = cursor.fetchall()  # Obtém os resultados da consulta
        cursor.close()  # Fecha o cursor
        db.close()  # Fecha a conexão com o banco de dados
        return resultados  # Retorna os resultados

    @QtCore.pyqtSlot()
    def consulta_documento_BD(documento):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tb_cliente WHERE tb_cli_doc = '{}'".format(documento))
        resultado = cursor.fetchone()
        cursor.close()  # Fecha o cursor
        db.close()  # Fecha a conexão com o banco de dados
        return resultado

    @QtCore.pyqtSlot()
    def consulta_nome(nome):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tb_cliente WHERE tb_cli_nome = '{}'".format(nome))
        resultado = cursor.fetchone()
        cursor.close()  # Fecha o cursor
        db.close()  # Fecha a conexão com o banco de dados
        return resultado