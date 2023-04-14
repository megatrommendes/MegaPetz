from Controller.AcessoCTR import AcessoCTR
from Controller.FuncionarioCTR import FuncionarioCTR
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormCadastroAcesso(object):
    def setupUi(self, FormCadastroAcesso):
        FormCadastroAcesso.setObjectName("FormCadastroAcesso")
        FormCadastroAcesso.setWindowModality(QtCore.Qt.ApplicationModal)
        FormCadastroAcesso.resize(780, 271)
        FormCadastroAcesso.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icon-cachorro-marrom-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormCadastroAcesso.setWindowIcon(icon)
        FormCadastroAcesso.setStyleSheet("background-color: rgb(21, 143, 157);")
        self.lista = QtWidgets.QTableWidget(FormCadastroAcesso)
        self.lista.setGeometry(QtCore.QRect(370, 10, 401, 251))
        self.lista.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.lista.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lista.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista.setProperty("showDropIndicator", False)
        self.lista.setGridStyle(QtCore.Qt.NoPen)
        self.lista.setObjectName("lista")
        self.lista.setColumnCount(2)
        self.lista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lista.setHorizontalHeaderItem(1, item)
        self.widget = QtWidgets.QWidget(FormCadastroAcesso)
        self.widget.setGeometry(QtCore.QRect(10, 10, 344, 100))
        self.widget.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.widget.setObjectName("widget")
        self.txt_cad_usuario = QtWidgets.QLineEdit(self.widget)
        self.txt_cad_usuario.setGeometry(QtCore.QRect(62, 63, 224, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_cad_usuario.setFont(font)
        self.txt_cad_usuario.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.txt_cad_usuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_cad_usuario.setPlaceholderText("")
        self.txt_cad_usuario.setObjectName("txt_cad_usuario")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(63, 6, 121, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_lista_usuarios = QtWidgets.QComboBox(self.widget)
        self.comboBox_lista_usuarios.setGeometry(QtCore.QRect(62, 22, 224, 20))
        self.comboBox_lista_usuarios.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.comboBox_lista_usuarios.setObjectName("comboBox_lista_usuarios")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(63, 47, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(11, 11, 41, 41))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/user.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.widget_2 = QtWidgets.QWidget(FormCadastroAcesso)
        self.widget_2.setGeometry(QtCore.QRect(10, 127, 344, 76))
        self.widget_2.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.widget_2.setObjectName("widget_2")
        self.cad_ace_checkBox_admim = QtWidgets.QCheckBox(self.widget_2)
        self.cad_ace_checkBox_admim.setGeometry(QtCore.QRect(63, 8, 263, 16))
        self.cad_ace_checkBox_admim.setObjectName("cad_ace_checkBox_admim")
        self.cad_ace_checkBox_usuario = QtWidgets.QCheckBox(self.widget_2)
        self.cad_ace_checkBox_usuario.setGeometry(QtCore.QRect(63, 29, 263, 16))
        self.cad_ace_checkBox_usuario.setObjectName("cad_ace_checkBox_usuario")
        self.cad_ace_checkBox_manual = QtWidgets.QCheckBox(self.widget_2)
        self.cad_ace_checkBox_manual.setGeometry(QtCore.QRect(63, 50, 263, 16))
        self.cad_ace_checkBox_manual.setObjectName("cad_ace_checkBox_manual")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(11, 10, 41, 41))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icons-ok.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.widget_3 = QtWidgets.QWidget(FormCadastroAcesso)
        self.widget_3.setGeometry(QtCore.QRect(10, 220, 344, 41))
        self.widget_3.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.widget_3.setObjectName("widget_3")
        self.btn_cad_acesso_sair = QtWidgets.QPushButton(self.widget_3)
        self.btn_cad_acesso_sair.setGeometry(QtCore.QRect(175, 11, 90, 20))
        self.btn_cad_acesso_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cad_acesso_sair.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 145, 10);\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(255, 145, 10);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icons-sinal-saída.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cad_acesso_sair.setIcon(icon1)
        self.btn_cad_acesso_sair.setObjectName("btn_cad_acesso_sair")
        self.btn_cad_acesso = QtWidgets.QPushButton(self.widget_3)
        self.btn_cad_acesso.setGeometry(QtCore.QRect(77, 11, 90, 20))
        self.btn_cad_acesso.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cad_acesso.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 145, 10);\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(255, 145, 10);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icon-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cad_acesso.setIcon(icon2)
        self.btn_cad_acesso.setObjectName("btn_cad_acesso")
        self.widget.raise_()
        self.lista.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()

        self.retranslateUi(FormCadastroAcesso)
        self.btn_cad_acesso_sair.clicked.connect(FormCadastroAcesso.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormCadastroAcesso)
        FormCadastroAcesso.setTabOrder(self.comboBox_lista_usuarios, self.txt_cad_usuario)
        FormCadastroAcesso.setTabOrder(self.txt_cad_usuario, self.cad_ace_checkBox_admim)
        FormCadastroAcesso.setTabOrder(self.cad_ace_checkBox_admim, self.cad_ace_checkBox_usuario)
        FormCadastroAcesso.setTabOrder(self.cad_ace_checkBox_usuario, self.cad_ace_checkBox_manual)
        FormCadastroAcesso.setTabOrder(self.cad_ace_checkBox_manual, self.lista)
        FormCadastroAcesso.setTabOrder(self.lista, self.btn_cad_acesso)
        FormCadastroAcesso.setTabOrder(self.btn_cad_acesso, self.btn_cad_acesso_sair)

        acesso = AcessoCTR
        query = acesso.ListaTodosAcessos(self)
        reg_acessos = query.fetchall()
        self.lista.setRowCount (len (reg_acessos))
        self.lista.setColumnCount (2)
        for i in range (0, len(reg_acessos)):
            for j in range (0, 2):
                self.lista.setItem (i, j, QtWidgets.QTableWidgetItem (str (reg_acessos[i][j])))

        funcionario = FuncionarioCTR
        query = funcionario.ListaTodosFuncionarios(self)
        reg_funcionario = query.fetchall()
        for funcionarios in reg_funcionario:
                self.comboBox_lista_usuarios.addItem(str(funcionarios[0]))

    def retranslateUi(self, FormCadastroAcesso):
        _translate = QtCore.QCoreApplication.translate
        FormCadastroAcesso.setWindowTitle(_translate("FormCadastroAcesso", "Cadastra Acesso"))
        item = self.lista.horizontalHeaderItem(0)
        item.setText(_translate("FormCadastroAcesso", "Acesso"))
        item = self.lista.horizontalHeaderItem(1)
        item.setText(_translate("FormCadastroAcesso", "Liberar"))
        self.label_5.setText(_translate("FormCadastroAcesso", "Funcionário"))
        self.label_6.setText(_translate("FormCadastroAcesso", "Pesquisa Nome"))
        self.cad_ace_checkBox_admim.setText(_translate("FormCadastroAcesso", "Permitir como administrador / acesso total"))
        self.cad_ace_checkBox_usuario.setText(_translate("FormCadastroAcesso", "Permitir como usuário / acesso parcial"))
        self.cad_ace_checkBox_manual.setText(_translate("FormCadastroAcesso", "Permitir seleionar / esolher acesso "))
        self.btn_cad_acesso_sair.setText(_translate("FormCadastroAcesso", "Sair"))
        self.btn_cad_acesso.setText(_translate("FormCadastroAcesso", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormCadastroAcesso = QtWidgets.QWidget()
    ui = Ui_FormCadastroAcesso()
    ui.setupUi(FormCadastroAcesso)
    FormCadastroAcesso.show()
    sys.exit(app.exec_())
