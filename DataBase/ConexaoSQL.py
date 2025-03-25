import sqlite3
from sqlite3 import Error


class ConexaoSQL:
    def getConexao(self):
        try:
            local = 'c:/MegaPetz/DataBase/MegaPetz-DB.db3'
            conexao = None
            conexao = sqlite3.connect(local)
            return conexao
        except Error as ex:
            print(ex)