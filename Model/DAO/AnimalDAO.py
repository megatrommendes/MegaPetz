from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesAuxiliares.AbilitaCampo import abilita_campo
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem
from Model.DAO.FuncoesAuxiliares.LimpaCampos import limpa_campos
from Model.DAO.FuncoesAuxiliares.ReposicionaFoco import reposiciona_foco


class AnimalDAO:
    @QtCore.pyqtSlot()
    def grava_dados_animal(self, operacao, cliente):
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

            if operacao == 'AC':
                query = """INSERT INTO tb_animal(tb_ani_doc, tb_ani_nome, tb_ani_especie, 
                           tb_ani_raca, tb_ani_cor, tb_ani_sexo, tb_ani_data_nasc, tb_tb_ani_idade, tb_ani_peso, 
                           tb_ani_mensalidade, tb_ani_data_cadastro, tb_ani_hora_cadastro, tb_ani_observacao) 
                           VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') """

                cursor.execute(query.format(cliente.tb_ani_doc,
                                            cliente.tb_ani_nome,
                                            cliente.tb_ani_especie,
                                            cliente.tb_ani_raca,
                                            cliente.tb_ani_cor,
                                            cliente.tb_ani_sexo,
                                            cliente.tb_data_nasc,
                                            cliente.tb_ani_idade,
                                            cliente.tb_ani_peso,
                                            cliente.tb_ani_mensalidade,
                                            cliente.tb_ani_data_cadastro,
                                            cliente.tb_ani_hora_cadastro,
                                            cliente.tb_ani_observacao))

                db.commit()
                pixmapFrontal = QPixmap(self.ui.imagemcamera_frontal_label.pixmap())
                pixmapVerso = QPixmap(self.ui.imagemcamera_tras_label.pixmap())
                caminhoFrontal = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(cliente.tb_cli_doc + '-FRENTE')
                caminhoVerso = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(cliente.tb_cli_doc + '-VERSO')

                # Salva a imagem no arquivo
                pixmapFrontal.save(caminhoFrontal)
                pixmapVerso.save(caminhoVerso)
                envia_mensagem('Cadastra Cliente', 'Cadastro salvo com sucesso!')

            elif operacao == 'AM':
                query = """UPDATE tb_animal SET tb_ani_nome = '{}', tb_ani_especie = '{}', tb_ani_raca 
                           = '{}', tb_ani_cor = '{}', tb_ani_sexo = '{}', tb_ani_data_nasc = '{}', tb_tb_ani_idade = '{}', 
                           tb_ani_peso = '{}', tb_ani_mensalidade = '{}', tb_ani_data_cadastro = '{}', 
                           tb_ani_hora_cadastro = '{}', tb_ani_observacao = '{}' WHERE 
                           tb_ani_doc = '{}' """

                cursor.execute(query.format(cliente.tb_ani_doc,
                                            cliente.tb_ani_nome,
                                            cliente.tb_ani_especie,
                                            cliente.tb_ani_raca,
                                            cliente.tb_ani_cor,
                                            cliente.tb_ani_sexo,
                                            cliente.tb_data_nasc,
                                            cliente.tb_ani_idade,
                                            cliente.tb_ani_peso,
                                            cliente.tb_ani_mensalidade,
                                            cliente.tb_ani_data_cadastro,
                                            cliente.tb_ani_hora_cadastro,
                                            cliente.tb_ani_observacao))
                db.commit()
                cursor.close()
                conn.close()
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
            if operacao == 'CM':
                envia_mensagem('Cadastra Mascote', 'Cadastro cancelado!')
            elif operacao == 'AM':
                envia_mensagem('Altera Mascote', 'Alteração cancelada!')

            limpa_campos(self)
            abilita_campo(self)
            reposiciona_foco(self)
        return False

    @QtCore.pyqtSlot()
    def seleciona_raca(especie):
        conn = ConexaoSQL()
        db = conn.getConexao()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tb_raca WHERE tb_raca_tipo = ? OR tb_raca_tipo = ?", ('Outros', especie))
        resultado = cursor.fetchall()
        cursor.close()
        db.close()
        return resultado

    @QtCore.pyqtSlot()
    def seleciona_cor(self):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tb_cor")
        resultado = cursor.fetchall()
        cursor.close()  # Fecha o cursor
        db.close()  # Fecha a conexão com o banco de dados

        # Ordenar os resultados em ordem alfabética
        resultado_ordenado = sorted(resultado, key=lambda cor: cor[1])

        return resultado_ordenado

    @QtCore.pyqtSlot()
    def seleciona_descricao_cor(cor_selecionada):
        conn = ConexaoSQL()
        db = conn.getConexao()
        cursor = db.cursor()
        cursor.execute("SELECT tb_cor_descricao FROM tb_cor WHERE tb_cor_cor = ?", (cor_selecionada,))
        resultado = cursor.fetchone()  # Usar fetchone() em vez de fetchall()
        cursor.close()
        db.close()
        if resultado:
            return resultado[0]  # Retorna somente o primeiro elemento da tupla resultado
        else:
            return ""  # Retorna uma string vazia caso não haja resultado



