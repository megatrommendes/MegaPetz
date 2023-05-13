from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


# Verifica se o numero do documento já existe na Base de Dados
def verifica_documento_bd(documento):
    conn = ConexaoSQL
    db = conn.getConexao(ConexaoSQL)
    cursor = db.cursor()
    cursor.execute("SELECT tb_cli_doc FROM tb_cliente WHERE tb_cli_doc = '{}'".format(documento))
    resultado = cursor.fetchone()

    if resultado is None:
        return True
    else:
        envia_mensagem('Cadastra Cliente', 'O documento informado já está cadastrado na base de dados!')
        return False
