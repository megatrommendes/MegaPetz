from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QPlainTextEdit, QLabel, QCheckBox

from Model.DAO.FuncoesAuxiliares.FormataCPF import formata_cpf
from Model.DAO.FuncoesAuxiliares.FormataData import formatar_data
from Model.DAO.FuncoesAuxiliares.FormataPeso import formata_peso
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from Model.DAO.FuncoesAuxiliares.SoNumero import so_numero
from Model.DAO.FuncoesAuxiliares.ValidaDia import valida_dia
from Model.DAO.FuncoesFormularios.FuncoesFormAnimal.ValidaCampoAnimal import valida_campo_animal
from Model.DAO.FuncoesFormularios.FuncoesFormAnimal.ValidaSalvarAnimal import validar_salvar_animal
from View.FrmCadastraAlteraAnimal import Ui_FrmCadastraAlteraAnimal
from View.Front_ConsultaClienteListagem import J_FrmConsultaClienteListagem
from Model.DAO.AnimalDAO import AnimalDAO


class J_FrmCadastraAlteraAnimal(QMainWindow):
    def __init__(self, operacao):
        super().__init__()
        self.ui = Ui_FrmCadastraAlteraAnimal()
        self.ui.setupUi(self)

        # Preencher o combobox de cor ao iniciar o formulário
        self.preencher_combobox_cor()

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

        # Conecta os Controles
        self.ui.btn_ani_listagem.clicked.connect(lambda: self.abre_FrmConsultaClienteListagem())
        self.ui.btn_ani_sair.clicked.connect(self.close)

        # Conecta o sinal currentTextChanged do QComboBox cad_ani_02_ob_especie à função preencher_combobox_racas
        self.ui.cad_ani_06_ob_especie.currentTextChanged.connect(lambda especie: preencher_combobox_racas(especie))

        self.ui.cad_ani_02_ob_peso.textChanged.connect(
            lambda text: self.ui.cad_ani_02_ob_peso.setText(formata_peso(text)))

        # Conectar o sinal textChanged ao método de validação valida o dia do pagamento
        self.ui.cad_ani_11_ob_dia_pagamento.textChanged.connect(
            lambda text: self.ui.cad_ani_11_ob_dia_pagamento.setText(valida_dia(text)))

        # Conecta o evento clicked do btn_ani_cadastrar à função validar_salvar_animal
        self.ui.btn_ani_cadastrar.clicked.connect(lambda: validar_salvar_animal(self, operacao))

        # Conecta o evento keyPressEvent do QMainWindow à função valida_campo
        self.keyPressEvent = lambda event: valida_campo_animal(self, event, operacao)

        self.ui.cad_ani_03_ob_nasc.textChanged.connect(
            lambda text: self.ui.cad_ani_03_ob_nasc.setText(formatar_data(text)))

        self.ui.cad_ani_04_ob_idade.textChanged.connect(
            lambda text: self.ui.cad_ani_04_ob_idade.setText(so_numero(text)))

        self.ui.cad_cli_00_doc_localiza.textChanged.connect(
            lambda text: self.ui.cad_cli_00_doc_localiza.setText(formata_cpf(text)))

        # Conecta o sinal currentTextChanged do QComboBox cad_ani_04_ob_cor à função atualizar_descricao_cor
        self.ui.cad_ani_09_ob_cor.currentTextChanged.connect(
            lambda cor_selecionada: atualizar_descricao_cor(cor_selecionada))


        # self.ui.cad_ani_04_ob_idade.installEventFilter(self)
        self.ui.cad_ani_03_ob_nasc.installEventFilter(self)

        self.ui.cad_ani_10_mensalista.clicked.connect(self.atualizar_campo_dia_pagamento)

        # Seleciona e exibe a descrição da cor quando a cor é selecionada
        def atualizar_descricao_cor(cor_selecionada):
            descricao = AnimalDAO.seleciona_descricao_cor(cor_selecionada)
            self.ui.cad_ani_descricao_cor.setPlainText(descricao)

        def preencher_combobox_racas(especie):
            resultado = AnimalDAO.seleciona_raca(especie)

            # Limpa os itens existentes no QComboBox
            self.ui.cad_ani_07_ob_raca.clear()

            # Adiciona cada raça ao QComboBox
            for raca in resultado:
                self.ui.cad_ani_07_ob_raca.addItem(raca[1])

        # Inserir a imagem no botão btn_cli_listagem e ajustar o tamanho
        image_path = "C:/MegaPetz/imagens/imagem_icones/user.png"
        pixmap = QtGui.QPixmap(image_path)
        # Define o tamanho desejado para a imagem
        target_size = QtCore.QSize(32, 32)  # Altere os valores para ajustar o tamanho
        pixmap = pixmap.scaled(target_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.btn_ani_listagem.setIcon(QtGui.QIcon(pixmap))
        self.ui.btn_ani_listagem.setIconSize(pixmap.size())

    def atualizar_campo_dia_pagamento(self):
        if self.ui.cad_ani_10_mensalista.isChecked():
            self.ui.cad_ani_11_ob_dia_pagamento.setEnabled(True)
        else:
            self.ui.cad_ani_11_ob_dia_pagamento.setText('')
            self.ui.cad_ani_11_ob_dia_pagamento.setEnabled(False)

    def abre_FrmConsultaClienteListagem(self):
        self.Frm_ConsultaClienteListagem = J_FrmConsultaClienteListagem(self, "CM")
        self.Frm_ConsultaClienteListagem.show()

    def preencher_combobox_cor(self):
        resultado = AnimalDAO.seleciona_cor(self)
        # Limpa os itens existentes no QComboBox
        self.ui.cad_ani_09_ob_cor.clear()
        # Adiciona um item vazio no início do QComboBox
        for cor in resultado:
            self.ui.cad_ani_09_ob_cor.addItem(cor[1])
        # Define o índice atual como -1 para não ter nenhum item selecionado
        self.ui.cad_ani_09_ob_cor.setCurrentIndex(-1)
