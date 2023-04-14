from Controller.ClienteCTR import ClienteCTR
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrmConsultaCliente(object):
    # Verifica qual campo esta com o foco e limpa os demais para a consulta
    def TXT_Doc_mousePressed(self, event):
        self.cons_txt_nome.setText('')

    # Verifica qual campo esta com o foco e limpa os demais para a consulta
    def TXT_Nome_mousePressed(self, event):
        self.cons_txt_doc.setText('')

    # Verifica qual campo esta com o foco e limpa os demais para a consulta
    def Combobox_Lista_mousePressed(self, event):
        self.cons_txt_doc.setText('')
        self.cons_txt_nome.setText('')
        self.comboBox_lista_clientes.clear()
        #adiciona todos os nomes dos clientes ao combobox
        cliente = ClienteCTR
        query = cliente.ListaTodosClientes(self)
        reg_cliente = query.fetchall()
        for clientes in reg_cliente:
            self.comboBox_lista_clientes.addItem(str(clientes[0]))
        self.comboBox_lista_clientes.showPopup()

    def btn_LocalizaCliente(self):
        doc = self.cons_txt_doc.text()
        lista = self.comboBox_lista_clientes.currentText()
        nome = self.cons_txt_nome.text()
        cliente = ClienteCTR
        cliente.LocalizaClientes(doc, lista, nome)
        self.cons_txt_doc.setText('')
        self.cons_txt_nome.setText('')
        self.comboBox_lista_clientes.setCurrentIndex(0)


    def setupUi(self, FrmConsultaCliente):
        FrmConsultaCliente.setObjectName("FrmConsultaCliente")
        #deixa o formulario em modal
        FrmConsultaCliente.setWindowModality(QtCore.Qt.ApplicationModal)
        FrmConsultaCliente.resize(470, 150)
        FrmConsultaCliente.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icon-cachorro-marrom-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmConsultaCliente.setWindowIcon(icon)
        FrmConsultaCliente.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.widget = QtWidgets.QWidget(FrmConsultaCliente)
        self.widget.setGeometry(QtCore.QRect(10, 10, 450, 131))
        self.widget.setStyleSheet("background-color: rgb(156, 202, 206);\n"
"border-radius:5px")
        self.widget.setObjectName("widget")
        self.btn_cons_Consultar = QtWidgets.QPushButton(self.widget)
        self.btn_cons_Consultar.setGeometry(QtCore.QRect(130, 98, 90, 20))
        self.btn_cons_Consultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cons_Consultar.setStyleSheet("QPushButton{\n"
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
        icon1.addPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icon-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_Consultar.setIcon(icon1)
        self.btn_cons_Consultar.setObjectName("btn_cons_Consultar")
        self.btn_cons_sair = QtWidgets.QPushButton(self.widget)
        self.btn_cons_sair.setGeometry(QtCore.QRect(228, 98, 90, 20))
        self.btn_cons_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cons_sair.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/icons-sinal-saída.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_sair.setIcon(icon2)
        self.btn_cons_sair.setObjectName("btn_cons_sair")
        self.cons_txt_nome = QtWidgets.QLineEdit(self.widget)
        self.cons_txt_nome.setGeometry(QtCore.QRect(61, 63, 330, 20))
        self.cons_txt_nome.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.cons_txt_nome.setMaxLength(60)
        self.cons_txt_nome.setObjectName("cons_cli_txt_nome")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(61, 9, 51, 16))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(61, 49, 100, 13))
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(10, 13, 41, 41))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:/bemlimpinho/imagens/user.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.comboBox_lista_clientes = QtWidgets.QComboBox(self.widget)
        self.comboBox_lista_clientes.setGeometry(QtCore.QRect(167, 24, 224, 20))
        self.comboBox_lista_clientes.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.comboBox_lista_clientes.setObjectName("comboBox_lista_clientes")
        self.comboBox_lista_clientes.setMaxVisibleItems (10)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(168, 10, 100, 13))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.cons_txt_doc = QtWidgets.QLineEdit(self.widget)
        self.cons_txt_doc.setGeometry(QtCore.QRect(60, 24, 101, 20))
        self.cons_txt_doc.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(21, 143, 157);\n"
"border-radius:5px")
        self.cons_txt_doc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cons_txt_doc.setObjectName("cons_txt_doc")

        self.retranslateUi(FrmConsultaCliente)
        self.btn_cons_sair.clicked.connect(FrmConsultaCliente.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FrmConsultaCliente)
        FrmConsultaCliente.setTabOrder(self.cons_txt_doc, self.comboBox_lista_clientes)
        FrmConsultaCliente.setTabOrder(self.comboBox_lista_clientes, self.cons_txt_nome)
        FrmConsultaCliente.setTabOrder(self.cons_txt_nome, self.btn_cons_Consultar)
        FrmConsultaCliente.setTabOrder(self.btn_cons_Consultar, self.btn_cons_sair)
        self.btn_cons_Consultar.clicked.connect (lambda: self.btn_LocalizaCliente())

        self.cons_txt_doc.mousePressEvent = self.TXT_Doc_mousePressed
        self.cons_txt_nome.mousePressEvent = self.TXT_Nome_mousePressed
        #self.comboBox_lista_clientes.activated.connect(self.Combobox_Lista_mousePressed)
        self.comboBox_lista_clientes.mousePressEvent = self.Combobox_Lista_mousePressed



    def retranslateUi(self, FrmConsultaCliente):
        _translate = QtCore.QCoreApplication.translate
        FrmConsultaCliente.setWindowTitle(_translate("FrmConsultaCliente", "Consulta Cliente"))
        self.btn_cons_Consultar.setText(_translate("FrmConsultaCliente", "ok"))
        self.btn_cons_sair.setText(_translate("FrmConsultaCliente", "Sair"))
        self.label_5.setText(_translate("FrmConsultaCliente", "RG / CPF"))
        self.label.setText(_translate("FrmConsultaCliente", "Pesquisa por Nome"))
        self.label_2.setText(_translate("FrmConsultaCliente", "Lista de Clientes"))
        self.cons_txt_doc.setInputMask(_translate("FrmConsultaCliente", "99999999999999"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmConsultaCliente = QtWidgets.QMainWindow()
    ui = Ui_FrmConsultaCliente()
    ui.setupUi(FrmConsultaCliente)
    FrmConsultaCliente.show()
    sys.exit(app.exec_())