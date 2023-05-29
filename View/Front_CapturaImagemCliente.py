import os
import cv2
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QMessageBox

from View.FrmCapturaImagemCliente import Ui_frmcapturaimagemcliente
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


class J_FrmCapturaImagemCliente(QWidget):
    def __init__(self, formulario, CPF, nomeImagem):
        super().__init__()
        # Define as variáveis 'documento' e 'frm_cliente' como atributos da classe
        self.formulario = formulario
        # Retorna veradeiro ou falso dependendo se a câmera foi inicializada
        self.camera_initializada = False
        # Instancia a classe Ui_frmcapturaimagemcliente() para criar a interface gráfica
        self.ui = Ui_frmcapturaimagemcliente()
        # Chama o método 'setupUi()' da classe Ui_frmcapturaimagemcliente() para configurar a interface
        self.ui.setupUi(self)

        # Atribui o número do CPF do cliente ao nome do arquivo da foto
        self.nome_arquivo = CPF + nomeImagem

        # Centraliza a imagem
        self.ui.fotoimagemcamera.setAlignment(QtCore.Qt.AlignCenter)

        # Inicializa a câmera
        self.camera = cv2.VideoCapture(0)  # instância um objeto cv2.VideoCapture
        # Verifica se a câmera foi inicializada com sucesso
        if not self.camera.isOpened():
            # Exibe uma mensagem de erro
            envia_mensagem("Erro de câmera",
                           "Não foi possível inicializar a câmera! Verifique se o dispositivo está ativo.")
            self.camera_initializada = False
        else:
            self.camera_initializada = True

        self.timer = QTimer(self)  # instância um objeto QTimer para atualização da imagem
        self.timer.timeout.connect(self.update_frame)  # conecta o sinal do timer a função update_frame
        self.timer.start(1)  # inicia o timer com intervalo de 1 milissegundo

        # Cria um layout para o QLabel que exibe a imagem
        self.imagemcamera_layout = QHBoxLayout(
            self.ui.fotoimagemcamera)  # instância um objeto QHBoxLayout para o QLabel
        self.imagemcamera_layout.setContentsMargins(0, 0, 0, 0)  # define as margens do layout como zero

        # Conecta os botôes
        # self.ui.btn_capturar.clicked.connect(self.captura_imagem)  # conecta o botão capturar a função captura_imagem
        self.ui.btn_capturar.clicked.connect(lambda: self.captura_imagem(formulario, nomeImagem))
        #self.ui.btn_salvar_imagem.clicked.connect(lambda: self.mens_bnt_salvar(nomeImagem))
        # conecta o botão salvar a função mens_bnt_salvar

        self.ui.btn_cancelar_imagem.clicked.connect(
            lambda: self.cancela_captura_imagem(nomeImagem))  # connect o botão cancelar a função cancela_captura_imagem
        self.ui.btn_sair_imagem.clicked.connect(self.close)  # conecta o botão sair a função close

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela
        self.setFixedSize(self.size())

    def verifica_camera(self):
        return self.camera_initializada

    @QtCore.pyqtSlot()
    def mens_bnt_salvar(self, nomeImagem):
        if self.timer.isActive():  # se o timer estiver ativo, para ele
            self.timer.stop()
        # Pergunta ao usuário se deseja salvar a imagem
        reply = QMessageBox.question(self, 'Salvar Imagem', "Deseja continuar e salvar a imagem?",
                                     QMessageBox.Ok | QMessageBox.Cancel,
                                     QMessageBox.Cancel)  # caixa de diálogo para confirmação do usuário
        if reply == QMessageBox.Ok:  # se o usuário confirmar a ação
            # Salva a imagem
            if self.salvar_imagem(
                    self.formulario,
                    nomeImagem):  # chama a função salvar_imagem para salvar a imagem e atualizar a interface
                self.mostra_mensagem("Imagem salva.", "Imagem salva com sucesso")
            else:
                self.mostra_mensagem("Não foi possível salvar a imagem.", "Erro ao salvar imagem")
        else:  # se o usuário cancelar a ação
            self.cancela_captura_imagem()  # cancela a captura de imagem
            self.mostra_mensagem("A imagem não foi salva.", "Imagem cancelada")

    @QtCore.pyqtSlot()
    def salvar_imagem(self, frm_cliente, nomeImagem):
        # Cria um objeto QPixmap com a imagem atual
        if nomeImagem == '-FRENTE':
            pixmap = QPixmap(frm_cliente.ui.imagemcamera_frontal_label.pixmap())
        else:
            pixmap = QPixmap(frm_cliente.ui.imagemcamera_tras_label.pixmap())

        # Define o caminho e nome do arquivo de saída sendo o nome do arquivo o número do documento do cliente
        caminho = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(self.nome_arquivo)

        # Salva a imagem no arquivo
        if pixmap.save(caminho):
            if nomeImagem == '-FRENTE':
                # Exibe a imagem no formulário J_FrmCadastroCliente
                frm_cliente.ui.imagemcamera_frontal_label.setPixmap(pixmap)
            else:
                frm_cliente.ui.imagemcamera_tras_label.setPixmap(pixmap)
            return True
        else:
            return False

    @QtCore.pyqtSlot()
    def mostra_mensagem(self, mensagem, titulo):
        # Cria uma caixa de mensagem com a mensagem fornecida e o título
        msgBox = QMessageBox()
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensagem)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec_()

    @QtCore.pyqtSlot()
    def update_frame(self):
        # Lê o próximo frame da câmera
        ret, frame = self.camera.read()

        # Verifica se o frame foi lido corretamente
        if ret:
            # Converte o frame para QImage e realiza o swap dos canais RGB
            self.ui.camera_image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()

            # Converte o QImage para QPixmap e redimensiona para o tamanho do QLabel
            pixmap = QPixmap.fromImage(self.ui.camera_image)
            pixmap = pixmap.scaled(self.ui.fotoimagemcamera.size(), Qt.KeepAspectRatio)

            # Define a imagem do QLabel com o QPixmap redimensionado
            self.ui.fotoimagemcamera.setPixmap(pixmap)

    @QtCore.pyqtSlot()
    def captura_imagem(self, frm_cliente, nomeImagem):
        # Captura uma imagem e exibe no QLabel
        ret, frame = self.camera.read()
        if ret:
            self.ui.captured_image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(self.ui.captured_image)
            pixmap = pixmap.scaled(self.ui.fotoimagemcamera.size(), Qt.KeepAspectRatio)
            self.ui.fotoimagemcamera.setPixmap(pixmap)
            self.timer.stop()
            pixmap = QPixmap(self.ui.fotoimagemcamera.pixmap())
            if nomeImagem == '-FRENTE':
                # Exibe a imagem no formulário J_FrmCadastroCliente
                frm_cliente.ui.imagemcamera_frontal_label.setPixmap(pixmap)
            else:
                frm_cliente.ui.imagemcamera_tras_label.setPixmap(pixmap)
            return True

    @QtCore.pyqtSlot()
    def cancela_captura_imagem(self, nomeImagem):
        pixmap = QPixmap('C:\\MegaPetz\\imagens\\imagem_icones\\icons-câmera.png')
        if nomeImagem == '-FRENTE':
            # Exibe a imagem no formulário J_FrmCadastroCliente
            self.formulario.ui.imagemcamera_frontal_label.setPixmap(pixmap)
        else:
            self.formulario.ui.imagemcamera_tras_label.setPixmap(pixmap)
        if self.timer.isActive():
            self.timer.stop()

        # Volta a exibir o frame da câmera
        if hasattr(self.ui, "captured_image"):
            delattr(self.ui, "captured_image")
        self.ui.fotoimagemcamera.clear()
        self.timer.start(1)

        # Remove o arquivo de imagem salvo
        #caminho = r'C:\MegaPetz\imagens\foto_cliente\{}.png'.format(self.nome_arquivo)
        #if os.path.exists(caminho):
        #    os.remove(caminho)

    @QtCore.pyqtSlot()
    def closeEvent(self, event):
        # Para a câmera quando o formulário é fechado
        self.camera.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Removido o código que cancela a ação da tecla Tab
    documento = "documento"
    window = J_FrmCapturaImagemCliente(documento)
    window.show()
    sys.exit(app.exec_())

'''
Este código define uma classe J_FormCapturaImagemClienteque herda da classe QWidget.
No construtor da classe, dois parâmetros são passados:frm_cliente e documento. 
Esses parâmetros são então atribuídos como atributos da classe.
Em seguida, a classe Ui_formcapturaimagemcliente()é instanciada,
o que permitirá que a interface gráfica seja criada a partir do arquivo de interface do Qt Designer. 
O método setupUi(self)da classeUi_formcapturaimagemcliente é chamado para configurar uma interface.
Essa classe é responsável por criar e gerenciar uma janela de captura de imagem para um cliente específico,
onde frm_cliente é a janela principal do programa e documento é uma variável que armazena informações
sobre o número do RG ou CPF.
'''
