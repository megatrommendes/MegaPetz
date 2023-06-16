from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPixmap, QColor
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QFileInfo
from qtpy import QtCore

from Model.DAO.ClienteDAO import ClienteDAO
from Model.DAO.FuncoesAuxiliares.ReposicionaFoco import reposiciona_foco
from View.FrmConsultaClienteListagem import Ui_FrmConsultaClienteListagem


class J_FrmConsultaClienteListagem(QMainWindow):
    def __init__(self, formulario, operacao):
        super().__init__()
        self.formulario = formulario
        self.operacao = operacao  # Definir o atributo 'operacao' com o valor passado como argumento
        self.cliente = Ui_FrmConsultaClienteListagem()
        self.ui = self.cliente
        self.ui.setupUi(self)

        self.setWindowFlags(
            QtCore.Qt.Window |  # Define que a janela é um objeto Qt de nível superior
            QtCore.Qt.CustomizeWindowHint |  # Permite personalizar a janela
            QtCore.Qt.WindowTitleHint |  # Exibe a barra de título da janela
            QtCore.Qt.WindowSystemMenuHint  # Exibe um menu de sistema para a janela
        )

        # Definida a janela com o tamanho atual e cancela o redimencionamento da janela atual
        self.setFixedSize(self.size())

        # Definir o cabeçalho das colunas
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nome', 'Endereço'])

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

        # Carregar todos os clientes
        self.lista_clientes = ClienteDAO.carrega_cliente(self)
        self.atualizar_tabela()

        # Atualizar o QLabel com o número de registros
        total_registros = len(self.lista_clientes)
        self.ui.total_registros_label.setText(str(total_registros) + ' ')

        # Criar um filtro de proxy para realizar a filtragem
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        self.ui.tableView_cliente.setModel(self.proxy_model)

        # Definir a coluna pelo qual será feita a ordenação
        self.proxy_model.setSortRole(Qt.DisplayRole)
        self.proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setSortLocaleAware(True)
        self.ui.tableView_cliente.setSortingEnabled(True)
        self.ui.tableView_cliente.sortByColumn(2, Qt.AscendingOrder)

        # Conectar o sinal textChanged do QLineEdit ao slot de filtro
        self.ui.cad_cli_00_nome_localiza.textChanged.connect(self.filtrar_tabela)

        # Conectar o sinal clicked do QTableView à função que atualiza os QLineEdit correspondentes
        self.ui.tableView_cliente.clicked.connect(self.atualizar_campos_dados_cliente)

        self.ui.btn_cli_sair.clicked.connect(lambda: self.formulario.ui.cad_cli_00_doc_localiza.setFocus())
        self.ui.btn_cli_sair.clicked.connect(self.close)
        self.ui.btn_cli_listagem.clicked.connect(lambda: (reposiciona_foco(self)))
        self.ui.btn_cli_listagem.clicked.connect(self.close)

    def atualizar_tabela(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Nome', 'Endereço'])
        for row, item in enumerate(self.lista_clientes):
            nome = item[1]
            endereco = item[2]
            row_items = [QStandardItem(str(nome)), QStandardItem(str(endereco))]
            self.model.appendRow(row_items)

            # Definir cores alternadas para as linhas da tabela
            if row % 2 == 0:
                # Cor para linhas pares (cinza claro)
                for column in range(self.model.columnCount()):
                    row_items[column].setBackground(QColor(103, 120, 138))  # Cinza claro
            else:
                # Cor para linhas ímpares (verde claro)
                for column in range(self.model.columnCount()):
                    row_items[column].setBackground(QColor(110, 165, 165))  # Verde claro

        self.ui.tableView_cliente.resizeColumnsToContents()

    def filtrar_tabela(self, text):
        # Define o texto de filtro para o QSortFilterProxyModel
        self.proxy_model.setFilterRegExp(text)
        # Define a coluna pela qual será feito o filtro (no caso, a coluna 0, correspondente ao nome)
        self.proxy_model.setFilterKeyColumn(0)

    def atualizar_campos_dados_cliente(self, index):
        # Obter o índice do modelo de proxy correspondente ao índice selecionado
        proxy_index = self.ui.tableView_cliente.model().mapToSource(index)

        # Obter a linha correspondente ao índice do modelo de proxy
        row = proxy_index.row()

        # Obter o cliente correspondente à linha selecionada no modelo original
        nome_index = self.model.index(row, 0)
        endereco_index = self.model.index(row, 1)
        cliente_nome = self.model.data(nome_index, Qt.DisplayRole)
        cliente_endereco = self.model.data(endereco_index, Qt.DisplayRole)

        # Restante do código para preencher os QLineEdit correspondentes com os dados do cliente
        nome = str(cliente_nome)
        endereco = str(cliente_endereco)

        # Preencher os demais campos conforme necessário
        cliente = self.lista_clientes[row]

        # Preencher os QLineEdit correspondentes com os dados do cliente
        nome = cliente[1]
        endereco = cliente[2]
        documento = cliente[0]
        numero = cliente[3]
        complemento = cliente[4]
        bairro = cliente[5]
        cidade = cliente[6]
        uf = cliente[7]
        cep = cliente[8]
        fone_pref = cliente[9]
        fone_alt = cliente[10]
        data_nasc = cliente[11]
        contato = cliente[12]
        obs = cliente[15]

        if self.operacao == "CC":
            # Preencher os QLineEdit correspondentes
            self.formulario.ui.cad_cli_03_ob_nome.setText(str(nome))
            self.formulario.ui.cad_cli_01_ob_doc.setText(str(documento))
            self.formulario.ui.cad_cli_05_ob_end.setText(str(endereco))
            self.formulario.ui.cad_cli_06_ob_num.setText(str(numero))
            self.formulario.ui.cad_cli_07_complemento.setText(str(complemento))
            self.formulario.ui.cad_cli_09_ob_bairro.setText(str(bairro))
            self.formulario.ui.cad_cli_10_ob_cidade.setText(str(cidade))
            self.formulario.ui.cad_cli_11_ob_fone_pref.setText(str(fone_pref))
            self.formulario.ui.cad_cli_12_fone_alt.setText(str(fone_alt))
            self.formulario.ui.cad_cli_13_contato.setText(str(contato))
            self.formulario.ui.cad_cli_14_obs.setPlainText(str(obs))
            self.formulario.ui.cad_cli_02_ob_nasc.setText(str(data_nasc))
            self.formulario.ui.cad_cli_04_ob_cep.setText(str(cep))

            # Exibir a imagem da frente do documento no QLabel
            file_path_frente = "C:/MegaPetz/imagens/foto_cliente/" + str(documento) + "-FRENTE.png"
            pixmap_frente = self.carregar_imagem(file_path_frente)
            self.formulario.ui.imagemcamera_frontal_label.setPixmap(pixmap_frente)

            # Exibir a imagem do verso do documento no QLabel
            file_path_verso = "C:/MegaPetz/imagens/foto_cliente/" + str(documento) + "-VERSO.png"
            pixmap_verso = self.carregar_imagem(file_path_verso)
            self.formulario.ui.imagemcamera_tras_label.setPixmap(pixmap_verso)

            # self.formulario.ui.cad_cli_00_doc_localiza.setFocus()

        if self.operacao == "CM":
            # Preencher os QLineEdit correspondentes
            self.formulario.ui.cad_cli_03_ob_nome.setText(str(nome))
            self.formulario.ui.cad_cli_05_ob_end.setText(str(endereco))
            self.formulario.ui.cad_cli_06_ob_num.setText(str(numero))
            # self.formulario.ui.cad_cli_07_complemento.setText(str(complemento))
            self.formulario.ui.cad_cli_11_ob_fone_pref.setText(str(fone_pref))

            # Verificar se algum item está selecionado
            if not proxy_index.isValid():
                self.formulario.ui.cad_cli_03_ob_nome.setText('')  # Limpar o campo de texto
                self.formulario.ui.cad_cli_03_ob_nome.setFocus()
            else:
                self.formulario.ui.cad_ani_01_ob_nome.setFocus()

    def carregar_imagem(self, file_path):
        file_info = QFileInfo(file_path)
        pixmap = QPixmap(file_path) if file_info.exists() else QPixmap(
            'C:/MegaPetz/imagens/imagem_icones/icons-câmera.png')
        return pixmap
