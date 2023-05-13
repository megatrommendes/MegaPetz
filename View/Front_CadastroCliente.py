import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QPlainTextEdit, QLabel
from View.FrmCadastroCliente import Ui_FrmCadastroCliente
from PyQt5.QtGui import QPixmap

# Funções auxiliares
from Model.DAO.FuncoesAuxiliares.CancelaTab import Cancela_Tab
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from Model.DAO.FuncoesAuxiliares.FormataData import formatar_data
from Model.DAO.FuncoesAuxiliares.SoNumero import so_numero
from Model.DAO.FuncoesAuxiliares.FormataCEP import formata_cep
from Model.DAO.FuncoesAuxiliares.FormataTelefone import formata_telefone
from Model.DAO.FuncoesAuxiliares.FormataCPF import formata_cpf
from Model.DAO.FuncoesAuxiliares.ValidaCampo import valida_campo
from Model.DAO.FuncoesFormularios.FuncoesFormCliente.ValidarSalvarCliente import validar_salvar_cliente


class J_FrmCadastroCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cliente = Ui_FrmCadastroCliente()
        self.ui = self.cliente
        self.ui.setupUi(self)

        # self.ui.btn_cli_cadastrar.clicked.connect(self.btn_cadastra)
        self.ui.btn_cli_sair.clicked.connect(self.close)
        self.ui.btn_abre_formcapturaimagem_frente.clicked.connect(lambda: self.abre_capturaimagemcliente('-FRENTE'))
        self.ui.btn_abre_formcapturaimagem_tras.clicked.connect(lambda: self.abre_capturaimagemcliente('-VERSO'))

        # Conecta o evento keyPressEvent do QMainWindow à função valida_campo
        self.keyPressEvent = lambda event: valida_campo(self, event)

        # Conecta o evento keyPressEvent do QMainWindow à função botao_salvar_cliente,
        # passando o valor da tecla enter pressionado
        # self.ui.btn_cli_cadastrar.clicked.connect(lambda: botao_salvar_cliente(self, None, Qt.LeftButton))
        self.ui.btn_cli_cadastrar.clicked.connect(lambda: validar_salvar_cliente(self))

        self.ui.cad_cli_02_ob_nasc.textChanged.connect(
            lambda text: self.ui.cad_cli_02_ob_nasc.setText(formatar_data(text)))

        self.ui.cad_cli_04_ob_cep.textChanged.connect(
            lambda text: self.ui.cad_cli_04_ob_cep.setText(formata_cep(text)))

        self.ui.cad_cli_06_ob_num.textChanged.connect(
            lambda text: self.ui.cad_cli_06_ob_num.setText(so_numero(text)))

        self.ui.cad_cli_11_ob_fone_pref.textChanged.connect(
            lambda text: self.ui.cad_cli_11_ob_fone_pref.setText(formata_telefone(text)))

        self.ui.cad_cli_12_fone_alt.textChanged.connect(
            lambda text: self.ui.cad_cli_12_fone_alt.setText(formata_telefone(text)))

        self.ui.cad_cli_01_ob_doc.textChanged.connect(
            lambda text: self.ui.cad_cli_01_ob_doc.setText(formata_cpf(text)))

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        # Exibe a imagem padrão caso não tenhauma imagem "Foto do cliente"
        pixmap = QPixmap('C:\\MegaPetz\\imagens\\imagem_icones\\icons-câmera.png')
        self.ui.imagemcamera_frontal_label.setPixmap(pixmap)
        self.ui.imagemcamera_tras_label.setPixmap(pixmap)

        # Centraliza a imagem
        self.ui.imagemcamera_frontal_label.setAlignment(QtCore.Qt.AlignCenter)

        # Centraliza a imagem
        self.ui.imagemcamera_tras_label.setAlignment(QtCore.Qt.AlignCenter)

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela atual
        self.setFixedSize(self.size())

        # Inicializa o formulário com o campo UF sempre com a sigla SP
        index = self.ui.cad_cli_08_UF.findText("SP", Qt.MatchStartsWith)
        if index != -1:
            self.ui.cad_cli_08_UF.setCurrentIndex(index)

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

    def abre_capturaimagemcliente(self, foto):
        # Importa a classe J_FormCapturaImagemCliente do arquivo Front_CapturaImagemCliente
        from View.Front_CapturaImagemCliente import J_FrmCapturaImagemCliente

        # Cria uma instância de J_FormCapturaImagemCliente, passando o próprio objeto J_FrmCadastroCliente como
        # self.frm_capturaimagemcliente = J_FrmCapturaImagemCliente(self.ui.cad_cli_01_ob_doc.text(), self)
        self.frm_capturaimagemcliente = J_FrmCapturaImagemCliente(self, self.ui.cad_cli_01_ob_doc.text(), foto)

        # Verifica se a câmera foi inicializada com sucesso
        if not self.frm_capturaimagemcliente.verifica_camera():
            # Fecha o formulário J_FormCapturaImagemCliente caso a câmera não tenha sido inicializada com sucesso
            self.frm_capturaimagemcliente.close()
        else:
            # Exibe o formulário J_FormCapturaImagemCliente caso a câmera tenha sido inicializada com sucesso
            self.frm_capturaimagemcliente.show()


if __name__ == "__main__":
    app = Cancela_Tab(sys.argv)  # chama a classe "Cancela_Tab" que cancela a ação da tecla Tab
    window = J_FrmCadastroCliente()
    window.show()
    sys.exit(app.exec_())