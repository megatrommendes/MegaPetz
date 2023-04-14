from DataBase.ConexaoSQL import ConexaoSQL

class AcessoDAO:
    def ListaTodosAcessos(self):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        sql = ("""SELECT tb_ace_acesso, tb_ace_liberar FROM tb_acesso""")
        query = cursor.execute(sql)

        return query