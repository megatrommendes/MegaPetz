from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


# Verifica se o numero do documento já existe na Base de Dados
def verifica_documento_bd(widgets, operacao, documento):
    conn = ConexaoSQL
    db = conn.getConexao(ConexaoSQL)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_cliente WHERE tb_cli_doc = '{}'".format(documento))
    resultado = cursor.fetchone()

    if operacao == "C":
        if resultado is None:
            return True
        else:
            envia_mensagem('Cadastra Cliente', 'O documento informado já está cadastrado.')
            return False

    if resultado:
        widgets['cad_cli_01_ob_doc'].setText(resultado[1])
        widgets['cad_cli_02_ob_nasc'].setText(resultado[12])
        widgets['cad_cli_03_ob_nome'].setText(resultado[2])
        widgets['cad_cli_04_ob_cep'].setText(str(resultado[9]))
        widgets['cad_cli_05_ob_end'].setText(resultado[3])
        widgets['cad_cli_06_ob_num'].setText(str(resultado[4]))
        widgets['cad_cli_07_complemento'].setText(resultado[5])
        widgets['cad_cli_09_ob_bairro'].setText(resultado[6])
        widgets['cad_cli_10_ob_cidade'].setText(resultado[7])
        widgets['cad_cli_11_ob_fone_pref'].setText(resultado[10])
        widgets['cad_cli_12_fone_alt'].setText(resultado[11])
        widgets['cad_cli_13_contato'].setText(resultado[13])
        widgets['cad_cli_14_obs'].setPlainText(resultado[16])

        if operacao == "L":
            widgets['cad_cli_08_UF'].setText(resultado[8])
            file_path = "C:/MegaPetz/imagens/foto_cliente/250.079.368-04-FRENTE.png"

            # Centraliza a imagem

            # Exibir a imagem no QLabel
            pixmap = QPixmap(file_path)
            widgets['imagemcamera_frontal_label'].setPixmap(pixmap)
            widgets['imagemcamera_frontal_label'].setAlignment(QtCore.Qt.AlignCenter)
            widgets['imagemcamera_frontal_label'].setScaledContents(True)


        if operacao == "A":
            uf = resultado[8]  # Obtenha o UF do resultado
            widgets['cad_cli_08_UF'].setCurrentText(uf)
            return True
    else:
        envia_mensagem('Cadastra Cliente', 'O documento informado não está cadastrado.')
        return False

