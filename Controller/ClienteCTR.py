from PyQt5 import QtCore

from Model.DTO.ClienteDTO import ClienteDTO
from Model.DAO.ClienteDAO import ClienteDAO


class ClienteCTR:
    @QtCore.pyqtSlot()
    def lista_cliente(self):
        clienteDAO = ClienteDAO
        query = clienteDAO.carrega_cliente(self)
        return query

    @QtCore.pyqtSlot()
    def LocalizaClientes(doc, lista, nome):
        clienteDTO = ClienteDTO
        clienteDTO.tb_cli_doc = doc
        clienteDTO.tb_cli_lista = lista
        clienteDTO.tb_cli_nome = nome
        clienteDAO = ClienteDAO
        clienteDAO.LocalizaClientes(ClienteDTO)

    @QtCore.pyqtSlot()
    def carrega_dados_cliente(self, operacao, documento, doc, nome, end, end_numero, complemento, bairro, cidade, UF, cep,
                              fone_preferencial,
                              fone_alternativo, data_nascimento, contato_alternativo, data_cadastro, hora_cadastro,
                              observacao):
        clieteDTO = ClienteDTO
        clieteDTO.tb_cli_doc = doc
        clieteDTO.tb_cli_nome = nome
        clieteDTO.tb_cli_endereco = end
        clieteDTO.tb_cli_numero = end_numero
        clieteDTO.tb_cli_complemento = complemento
        clieteDTO.tb_cli_bairro = bairro
        clieteDTO.tb_cli_cidade = cidade
        clieteDTO.tb_cli_uf = UF
        clieteDTO.tb_cli_cep = cep
        clieteDTO.tb_cli_fone_preferencial = fone_preferencial
        clieteDTO.tb_cli_fone_alternativo = fone_alternativo
        clieteDTO.tb_cli_data_nascimento = data_nascimento
        clieteDTO.tb_cli_contato_alternativo = contato_alternativo
        clieteDTO.tb_cli_data_cadastro = data_cadastro
        clieteDTO.tb_cli_hora_cadastro = hora_cadastro
        clieteDTO.tb_cli_observacao = observacao
        clienteDAO = ClienteDAO
        if clienteDAO.grava_dados_cliente(self, operacao, ClienteDTO) is False:
            return False
