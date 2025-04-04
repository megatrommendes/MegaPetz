from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmConsultaClienteListagem(object):
    def setupUi(self, FrmConsultaClienteListagem):
        FrmConsultaClienteListagem.setObjectName("FrmConsultaClienteListagem")
        FrmConsultaClienteListagem.setWindowModality(QtCore.Qt.ApplicationModal)
        FrmConsultaClienteListagem.resize(868, 544)
        FrmConsultaClienteListagem.setStyleSheet("background-color:rgb(42, 66, 76);")
        self.centralwidget = QtWidgets.QWidget(FrmConsultaClienteListagem)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(8, 102, 736, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.tableView_cliente = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableView_cliente.setFont(font)
        self.tableView_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableView_cliente.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.tableView_cliente.setFrameShape(QtWidgets.QFrame.Box)
        self.tableView_cliente.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView_cliente.setTabKeyNavigation(False)
        self.tableView_cliente.setAlternatingRowColors(False)
        self.tableView_cliente.setGridStyle(QtCore.Qt.NoPen)
        self.tableView_cliente.setObjectName("tableView_cliente")
        self.verticalLayout_2.addWidget(self.tableView_cliente)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 7, 851, 59))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 2, 0, 1, 3)
        self.total_registros_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_registros_label.setFont(font)
        self.total_registros_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.total_registros_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_registros_label.setObjectName("total_registros_label")
        self.gridLayout.addWidget(self.total_registros_label, 1, 1, 1, 2)
        self.cad_cli_00_doc_localiza_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_00_doc_localiza_label.setFont(font)
        self.cad_cli_00_doc_localiza_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_00_doc_localiza_label.setStyleSheet("color: rgb(255,255, 255);\n"
"background-color: rgb(0, 0, 47);\n"
"border-radius:3px")
        self.cad_cli_00_doc_localiza_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_00_doc_localiza_label.setObjectName("cad_cli_00_doc_localiza_label")
        self.gridLayout.addWidget(self.cad_cli_00_doc_localiza_label, 0, 1, 1, 2)
        self.cad_cli_00_nome_localiza = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_00_nome_localiza.setFont(font)
        self.cad_cli_00_nome_localiza.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_00_nome_localiza.setMaxLength(62)
        self.cad_cli_00_nome_localiza.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cad_cli_00_nome_localiza.setObjectName("cad_cli_00_nome_localiza")
        self.gridLayout.addWidget(self.cad_cli_00_nome_localiza, 1, 0, 1, 1)
        self.cad_cli_00_nome_localiza_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_00_nome_localiza_label.setFont(font)
        self.cad_cli_00_nome_localiza_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_00_nome_localiza_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_00_nome_localiza_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_00_nome_localiza_label.setObjectName("cad_cli_00_nome_localiza_label")
        self.gridLayout.addWidget(self.cad_cli_00_nome_localiza_label, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(756, 450, 101, 77))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.btn_cli_listagem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cli_listagem.setFont(font)
        self.btn_cli_listagem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cli_listagem.setStyleSheet("QPushButton{\n"
"color:rgb(255,255, 255);\n"
"background-color: rgb(0, 0, 47);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 47);\n"
"background-color: rgb(192, 206, 255);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 1, fx: 0.5, fy: 0.5,\n"
"        stop: 0 rgb(255, 255, 255));\n"
"    border-color: rgb(0, 0, 47);\n"
"border-radius:3px}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/Usuario/imagens/icon-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cli_listagem.setIcon(icon)
        self.btn_cli_listagem.setObjectName("btn_cli_listagem")
        self.verticalLayout.addWidget(self.btn_cli_listagem)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.btn_cli_sair = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cli_sair.setFont(font)
        self.btn_cli_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cli_sair.setStyleSheet("QPushButton{\n"
"color:rgb(255,255, 255);\n"
"background-color: rgb(0, 0, 47);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 47);\n"
"background-color: rgb(192, 206, 255);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qradialgradient(cx: 0.5, cy: 0.5, radius: 1, fx: 0.5, fy: 0.5,\n"
"        stop: 0 rgb(255, 255, 255));\n"
"    border-color: rgb(0, 0, 47);\n"
"border-radius:3px}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Users/Usuario/imagens/icons-sinal-saída.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cli_sair.setIcon(icon1)
        self.btn_cli_sair.setObjectName("btn_cli_sair")
        self.verticalLayout.addWidget(self.btn_cli_sair)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        FrmConsultaClienteListagem.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FrmConsultaClienteListagem)
        self.statusbar.setObjectName("statusbar")
        FrmConsultaClienteListagem.setStatusBar(self.statusbar)

        self.retranslateUi(FrmConsultaClienteListagem)
        QtCore.QMetaObject.connectSlotsByName(FrmConsultaClienteListagem)

    def retranslateUi(self, FrmConsultaClienteListagem):
        _translate = QtCore.QCoreApplication.translate
        FrmConsultaClienteListagem.setWindowTitle(_translate("FrmConsultaClienteListagem", "Lista de Clientes"))
        self.total_registros_label.setText(_translate("FrmConsultaClienteListagem", "0"))
        self.cad_cli_00_doc_localiza_label.setText(_translate("FrmConsultaClienteListagem", "     Registros    "))
        self.cad_cli_00_nome_localiza_label.setText(_translate("FrmConsultaClienteListagem", "Insira o Nome"))
        self.btn_cli_listagem.setText(_translate("FrmConsultaClienteListagem", "Confirmar"))
        self.btn_cli_sair.setText(_translate("FrmConsultaClienteListagem", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmConsultaClienteListagem = QtWidgets.QMainWindow()
    ui = Ui_FrmConsultaClienteListagem()
    ui.setupUi(FrmConsultaClienteListagem)
    FrmConsultaClienteListagem.show()
    sys.exit(app.exec_())
