from DataBase.ConexaoSQL import ConexaoSQL


def verifica_documento_bd(documento):
    conn = ConexaoSQL
    db = conn.getConexao(ConexaoSQL)
    cursor = db.cursor()
    cursor.execute("SELECT tb_cli_doc FROM tb_cliente WHERE tb_cli_doc = '{}'".format(documento))
    resultado = cursor.fetchone()

    if resultado is None:
        return True
    else:
        return False