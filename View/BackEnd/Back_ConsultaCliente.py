from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QPlainTextEdit, QLabel

# Funções auxiliares
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from Model.DAO.FuncoesAuxiliares.FormataCPF import formata_cpf
from Model.DAO.FuncoesAuxiliares.ReposicionaFoco import reposiciona_foco
from Model.DAO.FuncoesFormularios.FuncoesFormCliente.ValidaCampoCliente import valida_campo
from Model.DAO.FuncoesAuxiliares.LimpaCampos import limpa_campos
from View.FontEnd.FrmConsultaCliente import Ui_FrmConsultaCliente
# from Back_ConsultaClienteListagem import J_FrmConsultaClienteListagem


class J_FrmConsultaCliente(QMainWindow):
    def __init__(self, operacao):
        super().__init__()
        self.cliente = Ui_FrmConsultaCliente()
        self.ui = self.cliente
        self.ui.setupUi(self)

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela atual
        self.setFixedSize(self.size())

        # Centraliza a imagem
        self.ui.imagemcamera_frontal_label.setAlignment(QtCore.Qt.AlignCenter)

        # Centraliza a imagem
        self.ui.imagemcamera_tras_label.setAlignment(QtCore.Qt.AlignCenter)

        # Exibe a imagem padrão caso não tenha uma imagem "Foto do cliente"
        pixmap_camera = QPixmap('/imagens/imagem_icones/icons-câmera.png')
        self.ui.imagemcamera_frontal_label.setPixmap(pixmap_camera)
        self.ui.imagemcamera_tras_label.setPixmap(pixmap_camera)

        self.ui.btn_cli_listagem.clicked.connect(lambda: self.abre_FrmConsultaClienteListagem(operacao))

        self.ui.btn_cli_cancelar.clicked.connect(lambda: (limpa_campos(self), reposiciona_foco(self),
                                                          self.ui.imagemcamera_frontal_label.setPixmap(pixmap_camera),
                                                          self.ui.imagemcamera_tras_label.setPixmap(pixmap_camera)))

        self.ui.btn_cli_sair.clicked.connect(self.close)

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        for obj in self.findChildren((QLineEdit, QComboBox, QPlainTextEdit)):
            # Encontra o QLabel correspondente ao QLineEdit
            label_name = obj.objectName() + '_label'
            label = obj.parent().findChild(QLabel, label_name)
            # Instala um filtro de eventos nos objetos
            obj.installEventFilter(self)
            # Define a função lambda para o evento focusIn
            obj.focusInEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)
            # Define a função lambda para o evento focusOut
            obj.focusOutEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)

        # Conecta o evento keyPressEvent do QMainWindow à função valida_campo
        self.keyPressEvent = lambda event: valida_campo(self, event, operacao)

        self.ui.cad_cli_00_doc_localiza.textChanged.connect(
            lambda text: self.ui.cad_cli_00_doc_localiza.setText(formata_cpf(text)))

        # Inserir a imagem no botão btn_cli_listagem e ajustar o tamanho
        image_path = "/imagens/imagem_icones/user.png"
        pixmap = QtGui.QPixmap(image_path)
        # Define o tamanho desejado para a imagem
        target_size = QtCore.QSize(32, 32)  # Altere os valores para ajustar o tamanho
        pixmap = pixmap.scaled(target_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.btn_cli_listagem.setIcon(QtGui.QIcon(pixmap))
        self.ui.btn_cli_listagem.setIconSize(pixmap.size())

    def abre_FrmConsultaClienteListagem(self, operacao):
        self.Frm_ConsultaClienteListagem = J_FrmConsultaClienteListagem(self, operacao)
        self.Frm_ConsultaClienteListagem.show()


if __name__ == "__main__":
    window = Ui_FrmConsultaCliente()
    window.show()
