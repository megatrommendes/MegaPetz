from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QPlainTextEdit, QLabel, QCheckBox

from Model.DAO.FuncoesAuxiliares.FormataCPF import formata_cpf
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from Model.DAO.FuncoesFormularios.ValidaCampo import valida_campo
from View.FrmCadastraAlteraAnimal import Ui_FrmCadastraAlteraAnimal
from View.Front_ConsultaClienteListagem import J_FrmConsultaClienteListagem


class J_FrmCadastraAlteraAnimal(QMainWindow):
    def __init__(self, operacao):
        super().__init__()
        self.ui = Ui_FrmCadastraAlteraAnimal()
        self.ui.setupUi(self)

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela atual
        self.setFixedSize(self.size())

        for obj in self.findChildren((QLineEdit, QComboBox, QPlainTextEdit, QCheckBox)):
            # Encontra o QLabel correspondente ao QLineEdit
            label_name = obj.objectName() + '_label'
            label = obj.parent().findChild(QLabel, label_name)
            # Instala um filtro de eventos nos objetos
            obj.installEventFilter(self)
            # Define a função lambda para o evento focusIn
            obj.focusInEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)
            # Define a função lambda para o evento focusOut
            obj.focusOutEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)

        self.ui.btn_cli_listagem.clicked.connect(lambda: self.abre_FrmConsultaClienteListagem())
        self.ui.btn_cli_sair.clicked.connect(self.close)

        # Conecta o evento keyPressEvent do QMainWindow à função valida_campo
        self.keyPressEvent = lambda event: valida_campo(self, event, operacao)

        self.ui.cad_cli_00_doc_localiza.textChanged.connect(
            lambda text: self.ui.cad_cli_00_doc_localiza.setText(formata_cpf(text)))

        # Inserir a imagem no botão btn_cli_listagem e ajustar o tamanho
        image_path = "C:/MegaPetz/imagens/imagem_icones/user.png"
        pixmap = QtGui.QPixmap(image_path)
        # Define o tamanho desejado para a imagem
        target_size = QtCore.QSize(32, 32)  # Altere os valores para ajustar o tamanho
        pixmap = pixmap.scaled(target_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.btn_cli_listagem.setIcon(QtGui.QIcon(pixmap))
        self.ui.btn_cli_listagem.setIconSize(pixmap.size())

    def abre_FrmConsultaClienteListagem(self):
        self.Frm_ConsultaClienteListagem = J_FrmConsultaClienteListagem(self, "AC")
        self.Frm_ConsultaClienteListagem.show()
