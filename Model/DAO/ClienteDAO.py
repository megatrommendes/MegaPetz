from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem
from Model.DAO.FuncoesAuxiliares.ValidaData import valida_data
from Model.DAO.FuncoesAuxiliares.ValidaTelefone import valida_telefone
from Model.DAO.FuncoesAuxiliares.ValidaCPF import valida_cpf
from Model.DAO.FuncoesAuxiliares.ValidaTexto import valida_texto


class ClienteDAO:
    def ListaTodosClientes(self):
        conn = ConexaoSQL
        db = conn.getConexao(ConexaoSQL)
        cursor = db.cursor()
        sql = """SELECT tb_cli_nome FROM tb_cliente"""
        query = cursor.execute(sql)
        return query

    def CadastraClientes(cliente):
            conn = ConexaoSQL
            db = conn.getConexao(ConexaoSQL)
            cursor = db.cursor()
            cursor.execute("""INSERT INTO tb_cliente(tb_cli_doc, tb_cli_nome, tb_cli_endereco, 
                       tb_cli_numero, tb_cli_complemento, tb_cli_bairro, tb_cli_cidade, tb_cli_uf, tb_cli_cep, 
                       tb_cli_fone_preferencial, tb_cli_fone_alternativo, tb_cli_data_nascimento, 
                       tb_cli_contato_alternativo, tb_cli_data_cadastro, tb_cli_hora_cadastro, tb_cli_observacao) 
                       VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', 
                       '{}', '{}') """
                           .format(cliente.tb_cli_doc, cliente.tb_cli_nome,
                                   cliente.tb_cli_endereco,
                                   cliente.tb_cli_numero,
                                   cliente.tb_cli_complemento,
                                   cliente.tb_cli_bairro,
                                   cliente.tb_cli_cidade,
                                   cliente.tb_cli_uf,
                                   cliente.tb_cli_cep,
                                   cliente.tb_cli_fone_preferencial,
                                   cliente.tb_cli_fone_alternativo,
                                   cliente.tb_cli_data_nascimento,
                                   cliente.tb_cli_contato_alternativo,
                                   cliente.tb_cli_data_cadastro,
                                   cliente.tb_cli_hora_cadastro,
                                   cliente.tb_cli_observacao))
            db.commit()
            envia_mensagem('Cadastra Cliente','SALVO')

    def LocalizaClientes(cliente):
        # if cliente.tb_cli_doc.isdigit ():
        #        print("É numero")
        # else:
        #        print("Não é numero")
        print(cliente.cad_cli_01_ob_doc, cliente.tb_cli_lista, cliente.cad_cli_03_ob_nome)
