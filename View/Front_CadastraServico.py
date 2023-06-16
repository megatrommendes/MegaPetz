from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QLineEdit, QLabel, QPlainTextEdit
from PyQt5.QtGui import QStandardItemModel, QColor, QStandardItem
from PyQt5.QtCore import Qt

from Model.DAO.FuncoesFormularios.FuncoesFormServico.ValidaCampoServico import valida_campo_servico
from Model.DAO.FuncoesAuxiliares.FormataHora import formata_hora
from Model.DAO.FuncoesAuxiliares.FormataReal import formata_real
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from View.FrmCadastraServico import Ui_FrmCadastraServico


class J_FrmCadastraServico(QWidget):
    def __init__(self):
        super().__init__()
        self.cliente = Ui_FrmCadastraServico()
        self.ui = self.cliente
        self.ui.setupUi(self)

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        # Definida a janela com o tamanho atual e cancela o redimensionamento da janela atual
        self.setFixedSize(self.size())

        # Definir o cabeçalho das colunas
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Serviço', 'Período', 'Valor'])

        # Configurar o QTableView
        self.ui.tableView_cliente.setModel(self.model)
        self.ui.tableView_cliente.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_cliente.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableView_cliente.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableView_cliente.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Definir o estilo da tabela
        self.ui.tableView_cliente.setStyleSheet(
            "QTableView { background-color: rgb(40, 40, 40); color: black; "
            "border-style: solid; border-width: 1px; border-color: rgb(103, 120, 138); }"
            "QTableView::item:selected { background-color: rgb(0, 120, 215); color: white; }"
            "QTableView QHeaderView::section { background-color: rgb(40, 40, 40); color: white; }"
        )

        # Definir a cor do título da coluna
        self.ui.tableView_cliente.horizontalHeader().setStyleSheet("color: black;")

        # Definir o alongamento horizontal para as colunas
        self.ui.tableView_cliente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for obj in self.findChildren((QLineEdit, QPlainTextEdit)):
            # Encontra o QLabel correspondente ao QLineEdit
            label_name = obj.objectName() + '_label'
            label = obj.parent().findChild(QLabel, label_name)
            # Instala um filtro de eventos nos objetos
            obj.installEventFilter(self)
            # Define a função lambda para o evento focusIn
            obj.focusInEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)
            # Define a função lambda para o evento focusOut
            obj.focusOutEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)

        # Conecta o evento keyPressEvent do QWidget à função valida_campo
        self.keyPressEvent = lambda event: valida_campo_servico(self, event)

        self.ui.cad_serv_02_periodo.textChanged.connect(
            lambda text: self.ui.cad_serv_02_periodo.setText(formata_hora(text)))

        self.ui.cad_serv_03_ob_valor.textChanged.connect(
            lambda text: self.ui.cad_serv_03_ob_valor.setText(formata_real(text)))

        # Conexão do sinal clicked do botão ao slot de adicionar serviço
        self.ui.btn_serv_adicionar.clicked.connect(self.inserir_texto)

    def inserir_texto(self):
        # Obtenção do texto do QLineEdit
        servico = self.ui.cad_serv_04_ob_servico.text()
        periodo = self.ui.cad_serv_02_periodo.text()
        valor = self.ui.cad_serv_03_ob_valor.text()

        # Obtenção do modelo da tabela
        model = self.ui.tableView_cliente.model()

        # Verificação se o modelo é válido
        if not model:
            return

        # Inserção de uma nova linha no modelo
        model.insertRow(model.rowCount())

        # Criação dos objetos QStandardItem
        item_servico = QStandardItem(servico)
        item_periodo = QStandardItem(periodo)
        item_valor = QStandardItem(valor)

        # Definição dos objetos item nas células apropriadas
        model.setItem(model.rowCount() - 1, 0, item_servico)
        model.setItem(model.rowCount() - 1, 1, item_periodo)
        model.setItem(model.rowCount() - 1, 2, item_valor)

        # Definir cores alternadas para as linhas da tabela
        row_count = model.rowCount()
        for row in range(row_count):
            for column in range(model.columnCount()):
                item = model.item(row, column)
                if item is not None:
                    if row % 2 == 0:
                        # Cor para linhas pares (cinza claro)
                        item.setBackground(QColor(103, 120, 138))  # Cinza claro
                    else:
                        # Cor para linhas ímpares (verde claro)
                        item.setBackground(QColor(110, 165, 165))  # Verde claro

        # Atualização da exibição da tabela
        self.ui.tableView_cliente.viewport().update()

