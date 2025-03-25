from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAlteraSenha(object):
    def setupUi(self, FormAlteraSenha):
        FormAlteraSenha.setObjectName("FormAlteraSenha")
        FormAlteraSenha.setWindowModality(QtCore.Qt.ApplicationModal)
        FormAlteraSenha.resize(298, 229)
        FormAlteraSenha.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);")
        self.widget_2 = QtWidgets.QWidget(FormAlteraSenha)
        self.widget_2.setGeometry(QtCore.QRect(8, 8, 281, 71))
        self.widget_2.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.widget_2.setObjectName("widget_2")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(86, 9, 43, 16))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(12, 10, 61, 51))
        self.label_2.setStyleSheet("background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/icon_title.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(85, 27, 181, 25))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.comboBox.setObjectName("comboBox")
        self.widget = QtWidgets.QWidget(FormAlteraSenha)
        self.widget.setGeometry(QtCore.QRect(8, 89, 281, 131))
        self.widget.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.widget.setObjectName("widget")
        self.txt_conf_senha = QtWidgets.QLineEdit(self.widget)
        self.txt_conf_senha.setGeometry(QtCore.QRect(84, 67, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_conf_senha.setFont(font)
        self.txt_conf_senha.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.txt_conf_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_conf_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_conf_senha.setPlaceholderText("")
        self.txt_conf_senha.setObjectName("txt_conf_senha")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(83, 49, 121, 16))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setMidLineWidth(0)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(83, 9, 36, 16))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.btn_alt_senha = QtWidgets.QPushButton(self.widget)
        self.btn_alt_senha.setGeometry(QtCore.QRect(85, 97, 81, 20))
        self.btn_alt_senha.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_alt_senha.setStyleSheet("QPushButton{\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icones/icons8-add-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_alt_senha.setIcon(icon)
        self.btn_alt_senha.setObjectName("btn_alt_senha")
        self.txt_senha = QtWidgets.QLineEdit(self.widget)
        self.txt_senha.setGeometry(QtCore.QRect(84, 27, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setPlaceholderText("")
        self.txt_senha.setObjectName("txt_senha")
        self.btn_alt_senha_sair = QtWidgets.QPushButton(self.widget)
        self.btn_alt_senha_sair.setGeometry(QtCore.QRect(183, 97, 81, 20))
        self.btn_alt_senha_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_alt_senha_sair.setStyleSheet("QPushButton{\n"
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
        icon1.addPixmap(QtGui.QPixmap("../../icones/icons-sinal-de-saída-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_alt_senha_sair.setIcon(icon1)
        self.btn_alt_senha_sair.setObjectName("btn_alt_senha_sair")

        self.retranslateUi(FormAlteraSenha)
        self.btn_alt_senha_sair.clicked.connect(FormAlteraSenha.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormAlteraSenha)
        FormAlteraSenha.setTabOrder(self.comboBox, self.txt_senha)
        FormAlteraSenha.setTabOrder(self.txt_senha, self.txt_conf_senha)
        FormAlteraSenha.setTabOrder(self.txt_conf_senha, self.btn_alt_senha)
        FormAlteraSenha.setTabOrder(self.btn_alt_senha, self.btn_alt_senha_sair)

    def retranslateUi(self, FormAlteraSenha):
        _translate = QtCore.QCoreApplication.translate
        FormAlteraSenha.setWindowTitle(_translate("FormAlteraSenha", "Altera Senha"))
        self.label_7.setText(_translate("FormAlteraSenha", "Usuário"))
        self.label_6.setText(_translate("FormAlteraSenha", "<html><head/><body><p>Confirme a Senha</p></body></html>"))
        self.label_3.setText(_translate("FormAlteraSenha", "Senha"))
        self.btn_alt_senha.setText(_translate("FormAlteraSenha", "Alterar"))
        self.btn_alt_senha_sair.setText(_translate("FormAlteraSenha", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormAlteraSenha = QtWidgets.QWidget()
    ui = Ui_FormAlteraSenha()
    ui.setupUi(FormAlteraSenha)
    FormAlteraSenha.show()
    sys.exit(app.exec_())
