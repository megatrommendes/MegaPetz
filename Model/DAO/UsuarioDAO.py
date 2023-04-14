from DataBase.ConexaoSQL import ConexaoSQL
from Model.DAO.FuncoesDAO import RecebeMensagem

class UsuarioDAO:
    def CadastraUsuario(usuario):
        try:
            tit_Men = 'Cadastro de Usuário'

            conn = ConexaoSQL
            db = conn.getConexao(ConexaoSQL)
            cursor = db.cursor()

            if ((usuario.tb_usu_senha != '') and (usuario.confirma_senha != '')
                 and (usuario.tb_usu_usuario != '')):

                if (usuario.tb_usu_senha == usuario.confirma_senha):
                    cursor.execute ("""SELECT tb_usu_usuario FROM tb_usuario WHERE tb_usu_usuario =
                                 '{}'""".format(usuario.tb_usu_usuario))
                    var_usuario = cursor.fetchone()

                    if var_usuario == None:
                        cursor.execute("""INSERT INTO tb_usuario(tb_usu_usuario, tb_usu_senha) VALUES('{}', '{}')"""
                                       .format (usuario.tb_usu_usuario, usuario.tb_usu_senha))
                        db.commit()
                        RecebeMensagem(tit_Men, 'Usuário cadastrado com sucesso!')
                    else:
                        RecebeMensagem(tit_Men, 'Usuário já cadastrado, por favor informe outro usuário.')

                else:
                    RecebeMensagem(tit_Men, 'As senhas devem ser iguais, por favor tente novamente')

            else:
                RecebeMensagem(tit_Men, 'Por favor preencha os campos e tente novamente.')

            db.close()

        except Exception as e:
            print(e)
