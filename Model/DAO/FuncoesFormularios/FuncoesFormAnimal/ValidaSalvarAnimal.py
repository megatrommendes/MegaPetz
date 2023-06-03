from PyQt5.QtWidgets import QWidget, QLineEdit

from Model.DAO.FuncoesFormularios.FuncoesFormAnimal.ArmazenaDadosAnimal import armazena_dados_animal
from Model.DAO.FuncoesFormularios.FuncoesFormAnimal.ValidaDadosAnimal import valida_dados_animal


def validar_salvar_animal(self, operacao):
    # Valida os dados do cliente e armazena o número do documento
    ok, documento = valida_dados_animal(self, operacao)

    if ok:
        # Armazena o número do documento do cliente e envia para ClienteCTR
        armazena_dados_animal(self, operacao, documento)

        # Define o foco em um QLineEdit com 'doc' em seu nome
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QLineEdit) and 'doc' in widget.objectName():
                widget.setFocus()
                break
