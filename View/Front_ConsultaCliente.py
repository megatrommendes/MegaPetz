import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QPlainTextEdit, QLabel

# Funções auxiliares
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from Model.DAO.FuncoesAuxiliares.FormataCPF import formata_cpf
from Model.DAO.FuncoesAuxiliares.CancelaTab import Cancela_Tab
from Model.DAO.FuncoesAuxiliares.ReposicionaFoco import reposiciona_foco
from Model.DAO.FuncoesFormularios.ValidaCampo import valida_campo
from Model.DAO.FuncoesAuxiliares.LimpaCampos import limpa_campos
from View.FrmConsultaCliente import Ui_FrmConsultaCliente


class J_FrmConsultaCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cliente = Ui_FrmConsultaCliente()
        self.ui = self.cliente
        self.ui.setupUi(self)
        operacao = "L"  # Informa que o tipo de operação é referente aa consulta do fomuário consulta cliente

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela atual
        self.setFixedSize(self.size())

        # Centraliza a imagem
        self.ui.imagemcamera_frontal_label.setAlignment(QtCore.Qt.AlignCenter)

        # Centraliza a imagem
        self.ui.imagemcamera_tras_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.ui.btn_cli_cancelar.clicked.connect(lambda: (limpa_campos(self), reposiciona_foco(self)))
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


if __name__ == "__main__":
    app = Cancela_Tab(sys.argv)  # chama a classe "Cancela_Tab" que cancela a ação da tecla Tab
    window = Ui_FrmConsultaCliente()
    window.show()
    sys.exit(app.exec_())
