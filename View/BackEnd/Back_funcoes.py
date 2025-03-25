from  datetime import datetime
self.cad_cli_data_cadastro.setText(datetime.now().strftime('%d/%m/%Y  %H:%M'))


from PyQt5 import QtCore, QtWidgets

#from View.FrmCadastroAcesso import Ui_FormCadastroAcesso
#from View.FrmCadastroUsuario import Ui_FormCadastroUsuario
self.actionCadastra_Usu_rio.triggered.connect (self.teste)


#BD = sqlite3.connect('bemlimpinho_BD.db')

def func_val_login():
    BD = sqlite3.connect ('bemlimpinho_BD.db')
    cursor = BD.cursor ()
    cursor.execute ("""SELECT * FROM tb_usuario WHERE tb_usuario_id =
              '{}' AND tb_usuario_senha = '{}'""".format (formlogin.txt_usuario.text (), formlogin.txt_senha.text ()))
    dados_usuario = cursor.fetchone ()
    if dados_usuario != None:
        formlogin.close ()
    else:
        messagebox.showerror ('Erro ao logar', 'Usuário ou Senha incorreto, por favor tente novamente')
    BD.close ()

def func_cad_usuario():
    cursor = BD.cursor ()
    if (((formcadastrousuario.txt_cad_senha.text () != '') and (formcadastrousuario.txt_conf_senha.text () != '')
         and (formcadastrousuario.txt_cad_usuario.text () != ''))):
        if (formcadastrousuario.txt_cad_senha.text () == formcadastrousuario.txt_conf_senha.text ()):
            cursor.execute ("""SELECT tb_usuario_id FROM tb_usuario WHERE tb_usuario_id =
                             '{}'""".format (formcadastrousuario.txt_cad_usuario.text ()))
            var_rec_usu = cursor.fetchone ()
            if var_rec_usu == None:
                cursor.execute ("""INSERT INTO tb_usuario(tb_usuario_id, tb_usuario_senha) VALUES('{}', '{}')"""
                                .format (formcadastrousuario.txt_cad_usuario.text (),
                                         formcadastrousuario.txt_cad_senha.text ()))
                BD.commit ()
                #messagebox.showerror ('Cadastrar Usuário', 'Usuário cadastrado com sucesso!')
            else:
                messagebox.showerror ('Erro ao Cadastrar Usuário', 'Usuário já cadastrado')
        else:
            messagebox.showerror ('Erro ao Cadastrar Usuário', 'As senhas devem ser iguais, por favor tente novamente')
    else:
        messagebox.showerror ('Erro ao Cadastrar Usuário', 'Preencha os campos e tente novamente, por favor.')

def func_lista_usuarios():
    cursor = BD.cursor ()
    cursor.execute ("""SELECT tb_usuario_id FROM tb_usuario """)
    registros = cursor.fetchall ()
    for usuarios in registros:
        View.UI.FrmCadastroAcesso.comboBox_lista_usuarios.addItem (str (usuarios[0]))

def func_lista_acesso():
    # inseri dados na tabela
    cursor = BD.cursor ()
    cursor.execute ("""SELECT * FROM tb_usuario """)
    registros = cursor.fetchall()
    View.UI.FrmCadastroAcesso.lista.setRowCount (len (registros))
    View.UI.FrmCadastroAcesso.lista.setColumnCount (1)
    for i in range (0, len (registros)):
        for j in range (0, 1):
            View.UI.FrmCadastroAcesso.lista.setItem (i, j, QtWidgets.QTableWidgetItem (str (registros[i][j])))

if __name__ == "__main__":
    func_lista_usuarios()


    def CadastrarCliente(usuario):
        BD = sqlite3.connect ("DataBase/BemLimpinho-DB.db")
        cursor = BD.cursor ()
        cursor.execute("""INSERT INTO tb_usuario(tb_usu_usuario, tb_usu_senha) VALUES('{}', '{}')"""
                       .format(usuario.tb_usu_usuario, usuario.tb_usu_senha))
        BD.commit()
        print(usuario.tb_usu_usuario, usuario.tb_usu_senha)

    def ListaTodosUsuario(self):
        conn = ConexaoSQL
        db = conn.getConexao
        db.open()

        sql = "SELECT tb_usu_usuario FROM tb_usu_usuario"
        query = QSqlQuery(sql)
        return query

class UsuarioDAO:
    def CadastraUsuario(usuario):
        try:
            db = sqlite3.connect('/DataBase/BemLimpinho-DB.db3')
            cursor = db.cursor()
            cursor.execute("""INSERT INTO tb_usuario(tb_usu_usuario, tb_usu_senha) VALUES('{}', '{}')"""
                           .format (usuario.tb_usu_usuario, usuario.tb_usu_senha))
            db.commit()
        except Exception as e:
            print(e)


#import sqlite3

from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import *

class UsuarioDAO:
    def CadastraUsuario(usuario):
        try:
            conn = ConexaoSQL
            db = conn.getConexao(ConexaoSQL)
            db.open()

            query = QSqlQuery()
            query.prepare("""INSERT INTO tb_usuario(tb_usu_usuario, tb_usu_senha) VALUES('{}', '{}')"""
                           .format (usuario.tb_usu_usuario, usuario.tb_usu_senha))
            query.exec_()
            db.commit()
        except Exception as e:
            print(e)

        acesso = AcessoCTR
        query = acesso.ListaTodosAcessos(self)

        reg_encontrados = query.fetchall()
        self.lista.setRowCount (len (reg_encontrados))
        self.lista.setColumnCount (2)
        for i in range (0, len(reg_encontrados)):
            for j in range (0, 2):
                self.lista.setItem (i, j, QtWidgets.QTableWidgetItem (str (reg_encontrados[i][j])))


    #        local = 'C:/BemLimpinho/DataBase/BemLimpinho-DB.db3'
#        conn = None
#        conn = sqlite3.connect (local)
#        cursor = conn.cursor ()
#        self.comboBox_lista_usuarios.clear()
#        cursor.execute ("""SELECT * FROM tb_usuario """)
#        registros = cursor.fetchall ()
#        for usuarios in registros:
#            self.comboBox_lista_usuarios.addItem (str (usuarios[1]))
#        conn.close()
    def retranslateUi(self, FormCadastroAcesso):
        _translate = QtCore.QCoreApplication.translate
        FormCadastroAcesso.setWindowTitle(_translate("FormCadastroAcesso", "Cadastro de Acesso"))
        item = self.lista.horizontalHeaderItem(0)
        item.setText(_translate("FormCadastroAcesso", "Usuários"))
        self.label_5.setText(_translate("FormCadastroAcesso", "Lista de Usuários"))
        self.label_6.setText(_translate("FormCadastroAcesso", "Pesquisa por Nome"))
        self.btn_cad_acesso.setText(_translate("FormCadastroAcesso", "Cadastrar"))
        self.btn_cad_acesso_sair.setText(_translate("FormCadastroAcesso", "Sair"))

    def func_lista(self):
        try:
            local = 'C:/BemLimpinho/DataBase/BemLimpinho-DB.db3'
            conn = None
            conn = sqlite3.connect (local)
            cursor = conn.cursor ()
            cursor.execute ("""SELECT * FROM tb_usuarios """)
            registros = cursor.fetchall()
            self.lista.setRowCount (len (registros))
            self.lista.setColumnCount (1)
            for i in range (0, len (registros)):
                for j in range (0, 1):
                    self.lista.setItem (i, j, QtWidgets.QTableWidgetItem (str (registros[i][j])))
        except Exception as e:
                   print (e)
