from PyQt5.QtGui import QPixmap

from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem
from Model.DAO.ClienteDAO import ClienteDAO


def verifica_documento_bd(widgets, operacao, documento):
    """
    Verifica se o número do documento já existe na Base de Dados e realiza ações correspondentes.

    Args:
        widgets: Dicionário contendo os widgets utilizados na interface.
        operacao: String que representa a operação sendo realizada ("C" para cadastrar, "L" para listar, "A" para alterar).
        documento: Número do documento a ser verificado.

    Returns:
        Retorna True se o documento existe na Base de Dados e as informações correspondentes foram preenchidas corretamente.
        Retorna False caso contrário.
    """
    if operacao == "C":
        if ClienteDAO.consulta_documento_BD(documento) is None:
            return True
        else:
            envia_mensagem('Cadastra Cliente', 'O documento informado já está cadastrado.')
            return False

    if ClienteDAO.consulta_documento_BD(documento):
        resultado = ClienteDAO.consulta_documento_BD(documento)
        if operacao == 'CC':
            widgets['cad_cli_01_ob_doc'].setText(resultado[0])
            widgets['cad_cli_02_ob_nasc'].setText(resultado[11])
            widgets['cad_cli_03_ob_nome'].setText(resultado[1])
            widgets['cad_cli_04_ob_cep'].setText(str(resultado[8]))
            widgets['cad_cli_05_ob_end'].setText(str(resultado[2]))
            widgets['cad_cli_06_ob_num'].setText(str(resultado[3]))
            widgets['cad_cli_07_complemento'].setText(resultado[4])
            widgets['cad_cli_09_ob_bairro'].setText(resultado[5])
            widgets['cad_cli_10_ob_cidade'].setText(resultado[6])
            widgets['cad_cli_11_ob_fone_pref'].setText(resultado[9])
            widgets['cad_cli_12_fone_alt'].setText(resultado[10])
            widgets['cad_cli_13_contato'].setText(resultado[12])
            widgets['cad_cli_14_obs'].setPlainText(resultado[15])
            widgets['cad_cli_08_UF'].setText(resultado[7])

            # Exibir a imagem da frente do documento no QLabel
            file_path_FRENTE = "C:/MegaPetz/imagens/foto_cliente/" + documento + "-FRENTE.png"
            pixmap_frente = QPixmap(file_path_FRENTE)

            # Exibir a imagem do verso do documento no QLabel
            file_path_VERSO = "C:/MegaPetz/imagens/foto_cliente/" + documento + "-VERSO.png"
            pixmap_verso = QPixmap(file_path_VERSO)

            if pixmap_frente.isNull():
                file_path_FRENTE = "C:/MegaPetz/imagens/imagem_icones/icons-câmera.png"
                pixmap = QPixmap(file_path_FRENTE)
            else:
                widgets['imagemcamera_frontal_label'].setPixmap(pixmap_frente)

            if pixmap_verso.isNull():
                file_path_VERSO = "C:/MegaPetz/imagens/imagem_icones/icons-câmera.png"
                pixmap = QPixmap(file_path_VERSO)
            else:
                widgets['imagemcamera_tras_label'].setPixmap(pixmap_verso)
            return True

        if operacao == 'AC':
            resultado = ClienteDAO.consulta_documento_BD(documento)
            widgets['cad_cli_03_ob_nome'].setText(resultado[1])
            widgets['cad_cli_05_ob_end'].setText(str(resultado[2]))
            widgets['cad_cli_06_ob_num'].setText(str(resultado[3]))
            widgets['cad_cli_11_ob_fone_pref'].setText(resultado[9])
            return True

        if operacao == "A":
            uf_texto = resultado[7]  # Obtém a sigla do estado do resultado
            uf_index = widgets['cad_cli_08_UF'].findText(uf_texto)  # Obtém o índice do item com base no texto
            uf = widgets['cad_cli_08_UF'].itemText(uf_index)  # Obtém o texto do item com base no índice
            widgets['cad_cli_08_UF'].setCurrentText(uf)  # Define o texto do item selecionado

            # Exibir a imagem da frente do documento no QLabel

            file_path_FRENTE = "C:/MegaPetz/imagens/foto_cliente/" + documento + "-FRENTE.png"
            pixmap = QPixmap(file_path_FRENTE)
            if pixmap.isNull():
                file_path_FRENTE = "C:/MegaPetz/imagens/imagem_icones/icons-câmera.png"
                pixmap = QPixmap(file_path_FRENTE)
                widgets['imagemcamera_frontal_label'].setPixmap(pixmap)

                # Exibir a imagem do verso do documento no QLabel
                file_path_VERSO = "C:/MegaPetz/imagens/foto_cliente/" + documento + "-VERSO.png"
                pixmap = QPixmap(file_path_VERSO)

            if pixmap.isNull():
                file_path_VERSO = "C:/MegaPetz/imagens/imagem_icones/icons-câmera.png"
                pixmap = QPixmap(file_path_VERSO)
                widgets['imagemcamera_tras_label'].setPixmap(pixmap)

        return True
    else:
        envia_mensagem('Cadastra Cliente', 'O documento informado não está cadastrado.')
        return False
