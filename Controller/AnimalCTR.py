from PyQt5 import QtCore

from Model.DAO.AnimalDAO import AnimalDAO
from Model.DTO.AnimalDTO import AnimalDTO


class AnimalCTR:
    @QtCore.pyqtSlot()
    def carrega_dados_animal(operacao, documento, doc, nome, especie, raca, cor, sexo, data_nascimento,
                             idade, peso, mensalista, data_cadastro, hora_cadastro, observacao):
        animalDTO = AnimalDTO
        animalDTO.tb_ani_doc = doc
        animalDTO.tb_ani_nome = nome
        animalDTO.tb_ani_especie = especie
        animalDTO.tb_ani_raca = raca
        animalDTO.tb_ani_cor = cor
        animalDTO.tb_ani_sexo = sexo
        animalDTO.tb_ani_data_nasc = data_nascimento
        animalDTO.tb_ani_idade = idade
        animalDTO.tb_ani_paso = peso
        animalDTO.tb_ani_data_cadastro = data_cadastro
        animalDTO.tb_ani_hora_cadastro = hora_cadastro
        animalDTO.tb_ani_mensalista = mensalista
        animalDTO.tb_ani_observacao = observacao
        animalDAO = AnimalDAO

        if animalDAO.grava_dados_animal(operacao, documento,  animalDTO) is False:
            return False
