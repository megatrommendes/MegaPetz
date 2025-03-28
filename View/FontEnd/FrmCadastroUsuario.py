from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormCadastroUsuario(object):
    def setupUi(self, FormCadastroUsuario):
        FormCadastroUsuario.setObjectName("FormCadastroUsuario")
        FormCadastroUsuario.setWindowModality(QtCore.Qt.ApplicationModal)
        FormCadastroUsuario.resize(330, 228)
        FormCadastroUsuario.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagens/icon-cachorro-marrom-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormCadastroUsuario.setWindowIcon(icon)
        FormCadastroUsuario.setStyleSheet("background-color: rgb(21, 143, 157);")
        self.widget = QtWidgets.QWidget(FormCadastroUsuario)
        self.widget.setGeometry(QtCore.QRect(10, 9, 310, 210))
        self.widget.setStyleSheet("background-color: rgb(156, 202, 206);\n"
                                  "border-radius:5px")
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(62, 51, 43, 16))
        self.label_5.setObjectName("label_5")
        self.txt_conf_senha = QtWidgets.QLineEdit(self.widget)
        self.txt_conf_senha.setGeometry(QtCore.QRect(62, 147, 190, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_conf_senha.setFont(font)
        self.txt_conf_senha.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(21, 143, 157);\n"
                                          "border-radius:5px")
        self.txt_conf_senha.setMaxLength(12)
        self.txt_conf_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_conf_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_conf_senha.setPlaceholderText("")
        self.txt_conf_senha.setObjectName("txt_conf_senha")
        self.txt_cad_usuario = QtWidgets.QLineEdit(self.widget)
        self.txt_cad_usuario.setGeometry(QtCore.QRect(62, 66, 190, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_cad_usuario.setFont(font)
        self.txt_cad_usuario.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(21, 143, 157);\n"
                                           "border-radius:5px")
        self.txt_cad_usuario.setMaxLength(12)
        self.txt_cad_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_cad_usuario.setPlaceholderText("")
        self.txt_cad_usuario.setObjectName("txt_cad_usuario")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(62, 91, 36, 16))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.btn_cad_usu_cadastrar = QtWidgets.QPushButton(self.widget)
        self.btn_cad_usu_cadastrar.setGeometry(QtCore.QRect(62, 178, 90, 20))
        self.btn_cad_usu_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cad_usu_cadastrar.setStyleSheet("QPushButton{\n"
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
        icon1.addPixmap(QtGui.QPixmap("../imagens/icon-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cad_usu_cadastrar.setIcon(icon1)
        self.btn_cad_usu_cadastrar.setObjectName("btn_cad_usu_cadastrar")
        self.txt_cad_senha = QtWidgets.QLineEdit(self.widget)
        self.txt_cad_senha.setGeometry(QtCore.QRect(62, 106, 190, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_cad_senha.setFont(font)
        self.txt_cad_senha.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(21, 143, 157);\n"
                                         "border-radius:5px")
        self.txt_cad_senha.setMaxLength(12)
        self.txt_cad_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_cad_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_cad_senha.setPlaceholderText("")
        self.txt_cad_senha.setObjectName("txt_cad_senha")
        self.btn_cad_usu_sair = QtWidgets.QPushButton(self.widget)
        self.btn_cad_usu_sair.setGeometry(QtCore.QRect(161, 178, 90, 20))
        self.btn_cad_usu_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cad_usu_sair.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap("../imagens/icons-sinal-saída.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cad_usu_sair.setIcon(icon2)
        self.btn_cad_usu_sair.setObjectName("btn_cad_usu_sair")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(63, 11, 121, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_lista_usuarios = QtWidgets.QComboBox(self.widget)
        self.comboBox_lista_usuarios.setGeometry(QtCore.QRect(62, 26, 190, 20))
        self.comboBox_lista_usuarios.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                   "background-color: rgb(21, 143, 157);\n"
                                                   "border-radius:5px")
        self.comboBox_lista_usuarios.setObjectName("comboBox_lista_usuarios")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(63, 131, 71, 16))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(11, 14, 41, 41))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(21, 143, 157);\n"
                                    "border-radius:5px")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../imagens/user.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(FormCadastroUsuario)
        self.btn_cad_usu_sair.clicked.connect(FormCadastroUsuario.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormCadastroUsuario)
        FormCadastroUsuario.setTabOrder(self.comboBox_lista_usuarios, self.txt_cad_usuario)
        FormCadastroUsuario.setTabOrder(self.txt_cad_usuario, self.txt_cad_senha)
        FormCadastroUsuario.setTabOrder(self.txt_cad_senha, self.txt_conf_senha)
        FormCadastroUsuario.setTabOrder(self.txt_conf_senha, self.btn_cad_usu_cadastrar)
        FormCadastroUsuario.setTabOrder(self.btn_cad_usu_cadastrar, self.btn_cad_usu_sair)

    def retranslateUi(self, FormCadastroUsuario):
        _translate = QtCore.QCoreApplication.translate
        FormCadastroUsuario.setWindowTitle(_translate("FormCadastroUsuario", "Cadastra Usuário"))
        self.label_5.setText(_translate("FormCadastroUsuario", "Usuário"))
        self.label_3.setText(_translate("FormCadastroUsuario", "Senha"))
        self.btn_cad_usu_cadastrar.setText(_translate("FormCadastroUsuario", "OK"))
        self.btn_cad_usu_sair.setText(_translate("FormCadastroUsuario", "Sair"))
        self.label_7.setText(_translate("FormCadastroUsuario", "Funcionário"))
        self.label_4.setText(_translate("FormCadastroUsuario", "Confirma Senha"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FormCadastroUsuario = QtWidgets.QWidget()
    ui = Ui_FormCadastroUsuario()
    ui.setupUi(FormCadastroUsuario)
    FormCadastroUsuario.show()
    sys.exit(app.exec_())
