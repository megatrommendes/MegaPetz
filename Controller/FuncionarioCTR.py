from Model.DTO.FuncionarioDTO import FuncionarioDTO
from Model.DAO.FuncionarioDAO import FuncionarioDAO

class FuncionarioCTR:
    def ListaTodosFuncionarios(self):
        funcionarioDAO =FuncionarioDAO
        query = funcionarioDAO.ListaTodosFuncionarios(self)

        return query