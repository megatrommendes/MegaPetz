from Model.DTO.UsuarioDTO import UsuarioDTO
from Model.DAO.UsuarioDAO import UsuarioDAO

class UsuarioCTR:
    def CadastraUsuario(nome, senha, cfrmsenha):
        usuarioDTO = UsuarioDTO
        usuarioDTO.tb_usu_usuario = nome
        usuarioDTO.tb_usu_senha = senha
        usuarioDTO.confirma_senha = cfrmsenha
        usuarioDAO = UsuarioDAO
        usuarioDAO.CadastraUsuario(UsuarioDTO)

