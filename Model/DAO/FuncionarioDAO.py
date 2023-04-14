from DataBase.ConexaoSQL import ConexaoSQL

class FuncionarioDAO:
    def ListaTodosFuncionarios(self):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        sql = ("""SELECT tb_func_nome FROM tb_funcionario""")
        query = cursor.execute(sql)
        return query