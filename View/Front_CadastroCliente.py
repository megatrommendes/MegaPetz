import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QPlainTextEdit, QLabel, QWidget
from Model.DAO.FuncoesDAO import consulta_cep, Cancela_Tab, so_numero, valida_campo, formatar_data, formata_cep, \
    formata_telefone, formata_cpf, cor_foco
from View.FrmCadastroCliente import Ui_FrmCadastroCliente
from PyQt5.QtGui import QPixmap


class J_FrmCadastroCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cliente = Ui_FrmCadastroCliente()
        self.ui = self.cliente
        self.ui.setupUi(self)
        # self.ui.btn_cli_cadastrar.clicked.connect(self.btn_cadastra)
        self.ui.btn_cli_sair.clicked.connect(self.close)
        # self.ui.cad_cli_data_cadastro.setText(datetime.now().strftime('%d/%m/%Y  %H:%M h'))
        self.ui.cad_cli_txt_cepC.returnPressed.connect(self.recebe_dados_correio)
        self.ui.btn_abre_formcapturaimagem.clicked.connect(self.abre_capturaimagemcliente)

        # Conecta o evento keyPressEvent do QMainWindow à função valida_campo
        self.keyPressEvent = lambda event: valida_campo(self, event)

        self.ui.cad_cli_txt_data_nasc0D.textChanged.connect(
            lambda text: self.ui.cad_cli_txt_data_nasc0D.setText(formatar_data(text)))

        self.ui.cad_cli_txt_cepC.textChanged.connect(
            lambda text: self.ui.cad_cli_txt_cepC.setText(formata_cep(text)))

        self.ui.cad_cli_txt_end_numero02.textChanged.connect(
            lambda text: self.ui.cad_cli_txt_end_numero02.setText(so_numero(text)))

        self.ui.cad_cli_txt_fone_preferencial02.textChanged.connect(
            lambda text: self.ui.cad_cli_txt_fone_preferencial02.setText(formata_telefone(text)))

        self.ui.cad_cli_txt_fone_alternativo.textChanged.connect(
            lambda text: self.ui.cad_cli_txt_fone_alternativo.setText(formata_telefone(text)))

        self.ui.cad_cli_txt_doc01.textChanged.connect(
            lambda text: self.ui.cad_cli_txt_doc01.setText(formata_cpf(text)))

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        # Exibe a imagem padrão caso não tenhauma imagem "Foto do cliente"
        pixmap = QPixmap('C:\\MegaPetz\\imagens\\imagem_icones\\user.png')
        self.ui.imagemcamera_label.setPixmap(pixmap)

        # Centraliza a imagem
        self.ui.imagemcamera_label.setAlignment(QtCore.Qt.AlignCenter)

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela atual
        self.setFixedSize(self.size())

        # Inicializa o formulário com o campo UF sempre com a sigla SP
        index = self.ui.comboBox_UF.findText("SP", Qt.MatchStartsWith)
        if index != -1:
            self.ui.comboBox_UF.setCurrentIndex(index)

        for obj in self.findChildren((QLineEdit, QComboBox, QPlainTextEdit)):
            # Encontra o QLabel correspondente ao QLineEdit
            label_name = obj.objectName() + '_label'
            label = obj.parent().findChild(QLabel, label_name)
            # Instala um filtro de eventos nos objetos
            obj.installEventFilter(self)
            # Define a função lambda para o evento focusIn
            obj.focusInEvent = lambda event, obj=obj, label=label: cor_foco(obj, label, event)
            # Define a função lambda para o evento focusOut
            obj.focusOutEvent = lambda event, obj=obj, label=label: cor_foco(obj, label, event)

    @QtCore.pyqtSlot()
    def abre_capturaimagemcliente(self):
        # Importa a classe J_FormCapturaImagemCliente do arquivo Front_CapturaImagemCliente
        from View.Front_CapturaImagemCliente import J_FormCapturaImagemCliente

        # Cria uma instância de J_FormCapturaImagemCliente, passando o próprio objeto J_FrmCadastroCliente como
        # argumento
        self.frm_capturaimagemcliente = J_FormCapturaImagemCliente(self)

        # Verifica se a câmera foi inicializada com sucesso
        if not self.frm_capturaimagemcliente.verifica_camera():
            # Fecha o formulário J_FormCapturaImagemCliente caso a câmera não tenha sido inicializada com sucesso
            self.frm_capturaimagemcliente.close()
        else:
            # Exibe o formulário J_FormCapturaImagemCliente caso a câmera tenha sido inicializada com sucesso
            self.frm_capturaimagemcliente.show()

    @QtCore.pyqtSlot()
    def recebe_dados_correio(self):
        # Função para verifica se o CEP esta correto quando a tecla ENTER é pressionada,
        # e traz os dados caso seja encontrado na base dos correios
        logradouro, bairro, localidade, uf = consulta_cep(self.ui.cad_cli_txt_cepC.text())
        self.ui.cad_cli_txt_end02.setText(logradouro)
        self.ui.cad_cli_txt_bairro02.setText(bairro)
        self.ui.cad_cli_txt_cidade02.setText(localidade)
        index = self.ui.comboBox_UF.findText(uf, Qt.MatchStartsWith)
        if index != -1:
            self.ui.comboBox_UF.setCurrentIndex(index)
        # Verifica se a função retornou dados e caso não tenha limpa o campo CEP
        if logradouro == '':
            self.ui.cad_cli_txt_cepC.setText('')
            return False
        else:
            self.focusNextChild()
            return True


if __name__ == "__main__":
    app = Cancela_Tab(sys.argv)  # chama a classe "Cancela_Tab" que cancela a ação da tecla Tab
    window = J_FrmCadastroCliente()
    window.show()
    sys.exit(app.exec_())

'''
    @QtCore.pyqtSlot()
    def btn_cadastra(self):
        documento = self.ui.cad_cli_txt_doc01.text()
        nome = self.ui.cad_cli_txt_nome0.text()
        end = self.ui.cad_cli_txt_end0.text()
        end_numero = self.ui.cad_cli_txt_end_numero0.text()
        complemento = self.ui.cad_cli_txt_complemento.text()
        UF = str(self.ui.comboBox_UF.currentText())
        bairro = self.ui.cad_cli_txt_bairro0.text()
        cidade = self.ui.cad_cli_txt_cidade0.text()
        cep = self.ui.cad_cli_txt_cepC.text()
        fone_preferencial = self.ui.cad_cli_txt_fone_preferencial0.text()
        fone_alternativo = self.ui.cad_cli_txt_fone_alternativo.text()
        data_nascimento = self.ui.cad_cli_txt_data_nasc0D.text()
        contato_alternativo = self.ui.cad_cli_txt_contato_alternativo.text()
        data_cadastro = datetime.now().strftime('%d/%m/%Y')
        hora_cadastro = datetime.now().strftime('%H:%Mh')
        observacao = self.ui.cad_cli_txt_observacao.document().toPlainText()
        cliente = ClienteCTR
        if cliente.CadastraCliente(documento, nome, end, end_numero, complemento, bairro, cidade, UF, cep,
                                   fone_preferencial, fone_alternativo, data_nascimento, contato_alternativo,
                                   data_cadastro, hora_cadastro, observacao) != False:
            self.ui.cad_cli_txt_doc01.setText('')
            self.ui.cad_cli_txt_nome0.setText('')
            self.ui.cad_cli_txt_end0.setText('')
            self.ui.cad_cli_txt_end_numero0.setText('')
            self.ui.cad_cli_txt_complemento.setText('')
            self.ui.cad_cli_txt_bairro0.setText('')
            self.ui.cad_cli_txt_cidade0.setText('')
            self.ui.cad_cli_txt_cepC.setText('')
            self.ui.cad_cli_txt_fone_preferencial0.setText('')
            self.ui.cad_cli_txt_fone_alternativo.setText('')
            self.ui.cad_cli_txt_data_nasc0D.setText('')
            self.ui.cad_cli_txt_contato_alternativo.setText('')
            self.ui.cad_cli_txt_observacao.clear()
'''
