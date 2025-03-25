from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmConsultaCliente(object):
    def setupUi(self, FrmConsultaCliente):
        FrmConsultaCliente.setObjectName("FrmConsultaCliente")
        FrmConsultaCliente.setWindowModality(QtCore.Qt.ApplicationModal)
        FrmConsultaCliente.resize(813, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(49)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrmConsultaCliente.sizePolicy().hasHeightForWidth())
        FrmConsultaCliente.setSizePolicy(sizePolicy)
        FrmConsultaCliente.setMinimumSize(QtCore.QSize(490, 282))
        FrmConsultaCliente.setSizeIncrement(QtCore.QSize(490, 282))
        FrmConsultaCliente.setBaseSize(QtCore.QSize(490, 282))
        FrmConsultaCliente.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Users/Usuario/.designer/backup/imagens/icon-cachorro-marrom-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmConsultaCliente.setWindowIcon(icon)
        FrmConsultaCliente.setAutoFillBackground(False)
        FrmConsultaCliente.setStyleSheet("background-color:rgb(42, 66, 76);")
        FrmConsultaCliente.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(FrmConsultaCliente)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 14, 581, 576))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cad_cli_04_ob_cep_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_04_ob_cep_label.setFont(font)
        self.cad_cli_04_ob_cep_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_04_ob_cep_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_04_ob_cep_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_04_ob_cep_label.setObjectName("cad_cli_04_ob_cep_label")
        self.gridLayout_2.addWidget(self.cad_cli_04_ob_cep_label, 7, 4, 1, 1)
        self.cad_cli_09_ob_bairro_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_09_ob_bairro_label.setFont(font)
        self.cad_cli_09_ob_bairro_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_09_ob_bairro_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_09_ob_bairro_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_09_ob_bairro_label.setObjectName("cad_cli_09_ob_bairro_label")
        self.gridLayout_2.addWidget(self.cad_cli_09_ob_bairro_label, 13, 0, 1, 1)
        self.cad_cli_11_ob_fone_pref = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_11_ob_fone_pref.setFont(font)
        self.cad_cli_11_ob_fone_pref.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_11_ob_fone_pref.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_11_ob_fone_pref.setInputMask("")
        self.cad_cli_11_ob_fone_pref.setMaxLength(14)
        self.cad_cli_11_ob_fone_pref.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_11_ob_fone_pref.setReadOnly(True)
        self.cad_cli_11_ob_fone_pref.setObjectName("cad_cli_11_ob_fone_pref")
        self.gridLayout_2.addWidget(self.cad_cli_11_ob_fone_pref, 16, 0, 1, 1)
        self.cad_cli_05_ob_end = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_05_ob_end.setFont(font)
        self.cad_cli_05_ob_end.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_05_ob_end.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_05_ob_end.setMaxLength(62)
        self.cad_cli_05_ob_end.setReadOnly(True)
        self.cad_cli_05_ob_end.setObjectName("cad_cli_05_ob_end")
        self.gridLayout_2.addWidget(self.cad_cli_05_ob_end, 10, 0, 1, 4)
        self.cad_cli_13_contato_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_13_contato_label.setFont(font)
        self.cad_cli_13_contato_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_13_contato_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_13_contato_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_13_contato_label.setObjectName("cad_cli_13_contato_label")
        self.gridLayout_2.addWidget(self.cad_cli_13_contato_label, 15, 2, 1, 1)
        self.cad_cli_12_fone_alt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_12_fone_alt.setFont(font)
        self.cad_cli_12_fone_alt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_12_fone_alt.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_12_fone_alt.setInputMask("")
        self.cad_cli_12_fone_alt.setMaxLength(14)
        self.cad_cli_12_fone_alt.setCursorPosition(0)
        self.cad_cli_12_fone_alt.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_12_fone_alt.setReadOnly(True)
        self.cad_cli_12_fone_alt.setObjectName("cad_cli_12_fone_alt")
        self.gridLayout_2.addWidget(self.cad_cli_12_fone_alt, 16, 1, 1, 1)
        self.cad_cli_10_ob_cidade = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cad_cli_10_ob_cidade.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_10_ob_cidade.setFont(font)
        self.cad_cli_10_ob_cidade.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_10_ob_cidade.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_10_ob_cidade.setMaxLength(40)
        self.cad_cli_10_ob_cidade.setReadOnly(True)
        self.cad_cli_10_ob_cidade.setObjectName("cad_cli_10_ob_cidade")
        self.gridLayout_2.addWidget(self.cad_cli_10_ob_cidade, 14, 2, 1, 3)
        self.cad_cli_14_obs = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_14_obs.setFont(font)
        self.cad_cli_14_obs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_14_obs.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_14_obs.setObjectName("cad_cli_14_obs")
        self.gridLayout_2.addWidget(self.cad_cli_14_obs, 18, 0, 1, 5)
        self.cad_cli_04_ob_cep = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_04_ob_cep.setFont(font)
        self.cad_cli_04_ob_cep.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_04_ob_cep.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_04_ob_cep.setInputMask("")
        self.cad_cli_04_ob_cep.setMaxLength(9)
        self.cad_cli_04_ob_cep.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_04_ob_cep.setReadOnly(True)
        self.cad_cli_04_ob_cep.setObjectName("cad_cli_04_ob_cep")
        self.gridLayout_2.addWidget(self.cad_cli_04_ob_cep, 8, 4, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 2, 0, 1, 5)
        self.cad_cli_02_ob_nasc_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_02_ob_nasc_label.setFont(font)
        self.cad_cli_02_ob_nasc_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_02_ob_nasc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_02_ob_nasc_label.setObjectName("cad_cli_02_ob_nasc_label")
        self.gridLayout_2.addWidget(self.cad_cli_02_ob_nasc_label, 5, 1, 1, 1)
        self.cad_cli_08_UF = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_08_UF.setFont(font)
        self.cad_cli_08_UF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_08_UF.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(57, 57, 65);\n"
"border-radius:3px")
        self.cad_cli_08_UF.setInputMask("")
        self.cad_cli_08_UF.setMaxLength(14)
        self.cad_cli_08_UF.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cad_cli_08_UF.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_08_UF.setReadOnly(True)
        self.cad_cli_08_UF.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.cad_cli_08_UF.setObjectName("cad_cli_08_UF")
        self.gridLayout_2.addWidget(self.cad_cli_08_UF, 12, 4, 1, 1)
        self.cad_cli_07_complemento_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_07_complemento_label.setFont(font)
        self.cad_cli_07_complemento_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_07_complemento_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_07_complemento_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_07_complemento_label.setObjectName("cad_cli_07_complemento_label")
        self.gridLayout_2.addWidget(self.cad_cli_07_complemento_label, 11, 0, 1, 1)
        self.cad_cli_08_UF_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_08_UF_label.setFont(font)
        self.cad_cli_08_UF_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_08_UF_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_08_UF_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_08_UF_label.setObjectName("cad_cli_08_UF_label")
        self.gridLayout_2.addWidget(self.cad_cli_08_UF_label, 11, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.cad_cli_10_ob_cidade_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_10_ob_cidade_label.setFont(font)
        self.cad_cli_10_ob_cidade_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_10_ob_cidade_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_10_ob_cidade_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_10_ob_cidade_label.setObjectName("cad_cli_10_ob_cidade_label")
        self.gridLayout_2.addWidget(self.cad_cli_10_ob_cidade_label, 13, 2, 1, 1)
        self.cad_cli_07_complemento = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_07_complemento.setFont(font)
        self.cad_cli_07_complemento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_07_complemento.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_07_complemento.setMaxLength(62)
        self.cad_cli_07_complemento.setReadOnly(True)
        self.cad_cli_07_complemento.setObjectName("cad_cli_07_complemento")
        self.gridLayout_2.addWidget(self.cad_cli_07_complemento, 12, 0, 1, 4)
        self.cad_cli_01_ob_doc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_01_ob_doc.setFont(font)
        self.cad_cli_01_ob_doc.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_01_ob_doc.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_01_ob_doc.setInputMask("")
        self.cad_cli_01_ob_doc.setMaxLength(14)
        self.cad_cli_01_ob_doc.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cad_cli_01_ob_doc.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_01_ob_doc.setReadOnly(True)
        self.cad_cli_01_ob_doc.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.cad_cli_01_ob_doc.setObjectName("cad_cli_01_ob_doc")
        self.gridLayout_2.addWidget(self.cad_cli_01_ob_doc, 6, 0, 1, 1)
        self.cad_cli_03_ob_nome = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cad_cli_03_ob_nome.sizePolicy().hasHeightForWidth())
        self.cad_cli_03_ob_nome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_03_ob_nome.setFont(font)
        self.cad_cli_03_ob_nome.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_03_ob_nome.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_03_ob_nome.setMaxLength(62)
        self.cad_cli_03_ob_nome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cad_cli_03_ob_nome.setReadOnly(True)
        self.cad_cli_03_ob_nome.setObjectName("cad_cli_03_ob_nome")
        self.gridLayout_2.addWidget(self.cad_cli_03_ob_nome, 8, 0, 1, 4)
        self.cad_cli_11_ob_fone_pref_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_11_ob_fone_pref_label.setFont(font)
        self.cad_cli_11_ob_fone_pref_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_11_ob_fone_pref_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_11_ob_fone_pref_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_11_ob_fone_pref_label.setObjectName("cad_cli_11_ob_fone_pref_label")
        self.gridLayout_2.addWidget(self.cad_cli_11_ob_fone_pref_label, 15, 0, 1, 1)
        self.cad_cli_03_ob_nome_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_03_ob_nome_label.setFont(font)
        self.cad_cli_03_ob_nome_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_03_ob_nome_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_03_ob_nome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_03_ob_nome_label.setObjectName("cad_cli_03_ob_nome_label")
        self.gridLayout_2.addWidget(self.cad_cli_03_ob_nome_label, 7, 0, 1, 1)
        self.cad_cli_00_doc_localiza_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_00_doc_localiza_label.setFont(font)
        self.cad_cli_00_doc_localiza_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_00_doc_localiza_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_00_doc_localiza_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_00_doc_localiza_label.setObjectName("cad_cli_00_doc_localiza_label")
        self.gridLayout_2.addWidget(self.cad_cli_00_doc_localiza_label, 0, 0, 1, 1)
        self.cad_cli_05_ob_end_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_05_ob_end_label.setFont(font)
        self.cad_cli_05_ob_end_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_05_ob_end_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_05_ob_end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_05_ob_end_label.setObjectName("cad_cli_05_ob_end_label")
        self.gridLayout_2.addWidget(self.cad_cli_05_ob_end_label, 9, 0, 1, 1)
        self.cad_cli_14_obs_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_14_obs_label.setFont(font)
        self.cad_cli_14_obs_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_14_obs_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_14_obs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_14_obs_label.setObjectName("cad_cli_14_obs_label")
        self.gridLayout_2.addWidget(self.cad_cli_14_obs_label, 17, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 4, 0, 1, 5)
        self.cad_cli_13_contato = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.cad_cli_13_contato.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_13_contato.setFont(font)
        self.cad_cli_13_contato.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_13_contato.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_13_contato.setMaxLength(60)
        self.cad_cli_13_contato.setReadOnly(True)
        self.cad_cli_13_contato.setObjectName("cad_cli_13_contato")
        self.gridLayout_2.addWidget(self.cad_cli_13_contato, 16, 2, 1, 3)
        self.cad_cli_09_ob_bairro = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_09_ob_bairro.setFont(font)
        self.cad_cli_09_ob_bairro.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_09_ob_bairro.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_09_ob_bairro.setMaxLength(40)
        self.cad_cli_09_ob_bairro.setReadOnly(True)
        self.cad_cli_09_ob_bairro.setObjectName("cad_cli_09_ob_bairro")
        self.gridLayout_2.addWidget(self.cad_cli_09_ob_bairro, 14, 0, 1, 2)
        self.cad_cli_00_doc_localiza = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_00_doc_localiza.setFont(font)
        self.cad_cli_00_doc_localiza.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.cad_cli_00_doc_localiza.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_00_doc_localiza.setInputMask("")
        self.cad_cli_00_doc_localiza.setMaxLength(14)
        self.cad_cli_00_doc_localiza.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cad_cli_00_doc_localiza.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_00_doc_localiza.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.cad_cli_00_doc_localiza.setObjectName("cad_cli_00_doc_localiza")
        self.gridLayout_2.addWidget(self.cad_cli_00_doc_localiza, 1, 0, 1, 1)
        self.cad_cli_01_ob_doc_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_01_ob_doc_label.setFont(font)
        self.cad_cli_01_ob_doc_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_01_ob_doc_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_01_ob_doc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_01_ob_doc_label.setObjectName("cad_cli_01_ob_doc_label")
        self.gridLayout_2.addWidget(self.cad_cli_01_ob_doc_label, 5, 0, 1, 1)
        self.cad_cli_02_ob_nasc = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_02_ob_nasc.setFont(font)
        self.cad_cli_02_ob_nasc.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_02_ob_nasc.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_02_ob_nasc.setInputMask("")
        self.cad_cli_02_ob_nasc.setText("")
        self.cad_cli_02_ob_nasc.setMaxLength(10)
        self.cad_cli_02_ob_nasc.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_02_ob_nasc.setReadOnly(True)
        self.cad_cli_02_ob_nasc.setObjectName("cad_cli_02_ob_nasc")
        self.gridLayout_2.addWidget(self.cad_cli_02_ob_nasc, 6, 1, 1, 1)
        self.cad_cli_06_ob_num_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_06_ob_num_label.setFont(font)
        self.cad_cli_06_ob_num_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_06_ob_num_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_06_ob_num_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_06_ob_num_label.setObjectName("cad_cli_06_ob_num_label")
        self.gridLayout_2.addWidget(self.cad_cli_06_ob_num_label, 9, 4, 1, 1)
        self.cad_cli_06_ob_num = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_06_ob_num.setFont(font)
        self.cad_cli_06_ob_num.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cad_cli_06_ob_num.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.cad_cli_06_ob_num.setInputMask("")
        self.cad_cli_06_ob_num.setMaxLength(5)
        self.cad_cli_06_ob_num.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_06_ob_num.setReadOnly(True)
        self.cad_cli_06_ob_num.setObjectName("cad_cli_06_ob_num")
        self.gridLayout_2.addWidget(self.cad_cli_06_ob_num, 10, 4, 1, 1)
        self.cad_cli_12_fone_alt_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_12_fone_alt_label.setFont(font)
        self.cad_cli_12_fone_alt_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_12_fone_alt_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_12_fone_alt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_12_fone_alt_label.setObjectName("cad_cli_12_fone_alt_label")
        self.gridLayout_2.addWidget(self.cad_cli_12_fone_alt_label, 15, 1, 1, 1)
        self.btn_cli_listagem = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cli_listagem.sizePolicy().hasHeightForWidth())
        self.btn_cli_listagem.setSizePolicy(sizePolicy)
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
        self.btn_cli_listagem.setObjectName("btn_cli_listagem")
        self.gridLayout_2.addWidget(self.btn_cli_listagem, 0, 1, 2, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(611, 260, 191, 131))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.imagemcamera_tras_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.imagemcamera_tras_label.setMinimumSize(QtCore.QSize(0, 0))
        self.imagemcamera_tras_label.setMaximumSize(QtCore.QSize(500, 500))
        self.imagemcamera_tras_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.imagemcamera_tras_label.setText("")
        self.imagemcamera_tras_label.setObjectName("imagemcamera_tras_label")
        self.gridLayout_5.addWidget(self.imagemcamera_tras_label, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(611, 41, 191, 130))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.imagemcamera_frontal_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.imagemcamera_frontal_label.setMinimumSize(QtCore.QSize(0, 0))
        self.imagemcamera_frontal_label.setMaximumSize(QtCore.QSize(500, 500))
        self.imagemcamera_frontal_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"        background-color: transparent;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-color: rgb(103, 120, 138);\n"
"border-radius:3px;")
        self.imagemcamera_frontal_label.setText("")
        self.imagemcamera_frontal_label.setObjectName("imagemcamera_frontal_label")
        self.gridLayout_3.addWidget(self.imagemcamera_frontal_label, 1, 2, 1, 1)
        self.cad_cli_imagem_frente = QtWidgets.QLabel(self.centralwidget)
        self.cad_cli_imagem_frente.setGeometry(QtCore.QRect(611, 15, 191, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_imagem_frente.setFont(font)
        self.cad_cli_imagem_frente.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_imagem_frente.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_imagem_frente.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_imagem_frente.setObjectName("cad_cli_imagem_frente")
        self.cad_cli_imagem_tras = QtWidgets.QLabel(self.centralwidget)
        self.cad_cli_imagem_tras.setGeometry(QtCore.QRect(611, 235, 191, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cad_cli_imagem_tras.setFont(font)
        self.cad_cli_imagem_tras.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cad_cli_imagem_tras.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(110, 165, 165);\n"
"border-radius:3px")
        self.cad_cli_imagem_tras.setAlignment(QtCore.Qt.AlignCenter)
        self.cad_cli_imagem_tras.setObjectName("cad_cli_imagem_tras")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(591, 14, 20, 576))
        self.line_4.setStyleSheet("")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(611, 472, 191, 10))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(606, 585, 191, 10))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(658, 490, 101, 97))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget_5)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_4.addWidget(self.line_9, 0, 0, 1, 1)
        self.btn_cli_cancelar = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cli_cancelar.setFont(font)
        self.btn_cli_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cli_cancelar.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Users/Usuario/imagens/icon-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cli_cancelar.setIcon(icon2)
        self.btn_cli_cancelar.setObjectName("btn_cli_cancelar")
        self.gridLayout_4.addWidget(self.btn_cli_cancelar, 1, 0, 1, 1)
        self.btn_cli_sair = QtWidgets.QPushButton(self.gridLayoutWidget_5)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Users/Usuario/imagens/icons-sinal-saída.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cli_sair.setIcon(icon3)
        self.btn_cli_sair.setObjectName("btn_cli_sair")
        self.gridLayout_4.addWidget(self.btn_cli_sair, 3, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_5)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_4.addWidget(self.line_11, 2, 0, 1, 1)
        FrmConsultaCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmConsultaCliente)
        QtCore.QMetaObject.connectSlotsByName(FrmConsultaCliente)

    def retranslateUi(self, FrmConsultaCliente):
        _translate = QtCore.QCoreApplication.translate
        FrmConsultaCliente.setWindowTitle(_translate("FrmConsultaCliente", "Consulta Cliente"))
        self.cad_cli_04_ob_cep_label.setText(_translate("FrmConsultaCliente", "CEP"))
        self.cad_cli_09_ob_bairro_label.setText(_translate("FrmConsultaCliente", "Bairro"))
        self.cad_cli_13_contato_label.setText(_translate("FrmConsultaCliente", "Nome do Contato"))
        self.cad_cli_02_ob_nasc_label.setText(_translate("FrmConsultaCliente", "Data. Nascimento"))
        self.cad_cli_07_complemento_label.setText(_translate("FrmConsultaCliente", "Complemento"))
        self.cad_cli_08_UF_label.setText(_translate("FrmConsultaCliente", "Estado"))
        self.cad_cli_10_ob_cidade_label.setText(_translate("FrmConsultaCliente", "Cidade"))
        self.cad_cli_11_ob_fone_pref_label.setText(_translate("FrmConsultaCliente", "Tel. Preferêncial"))
        self.cad_cli_03_ob_nome_label.setText(_translate("FrmConsultaCliente", "Nome"))
        self.cad_cli_00_doc_localiza_label.setText(_translate("FrmConsultaCliente", "Insira o CPF"))
        self.cad_cli_05_ob_end_label.setText(_translate("FrmConsultaCliente", "Endereço"))
        self.cad_cli_14_obs_label.setText(_translate("FrmConsultaCliente", "Observações"))
        self.cad_cli_01_ob_doc_label.setText(_translate("FrmConsultaCliente", "CPF"))
        self.cad_cli_06_ob_num_label.setText(_translate("FrmConsultaCliente", "Número"))
        self.cad_cli_12_fone_alt_label.setText(_translate("FrmConsultaCliente", "Tel. Alternativo"))
        self.btn_cli_listagem.setText(_translate("FrmConsultaCliente", "Pesquisa Cliente "))
        self.cad_cli_imagem_frente.setText(_translate("FrmConsultaCliente", "Foto Frente"))
        self.cad_cli_imagem_tras.setText(_translate("FrmConsultaCliente", "Foto Verso"))
        self.btn_cli_cancelar.setText(_translate("FrmConsultaCliente", "Cancelar"))
        self.btn_cli_sair.setText(_translate("FrmConsultaCliente", "Sair"))
