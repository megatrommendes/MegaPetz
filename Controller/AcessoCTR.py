from Model.DTO.AcessoDTO import AcessoDTO
from Model.DAO.AcessoDAO import AcessoDAO

class AcessoCTR:
    def ListaTodosAcessos(self):
        acessoDAO = AcessoDAO
        query = acessoDAO.ListaTodosAcessos(self)

        return query
