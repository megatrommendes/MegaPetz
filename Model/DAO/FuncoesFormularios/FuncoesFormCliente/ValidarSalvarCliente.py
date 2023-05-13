from PyQt5.QtWidgets import QWidget, QLineEdit

from Model.DAO.FuncoesFormularios.FuncoesFormCliente.ValidaDadosCliente import valida_dados_cliente
from Model.DAO.FuncoesFormularios.FuncoesFormCliente.ArmazenaDadosCliente import armazena_dados_cliente


def validar_salvar_cliente(self):
    # Valida os dados do cliente e armazena o número do documento
    ok, documento = valida_dados_cliente(self)

    if ok:
        # Armazena o número do documento do cliente e envia para ClienteCTR
        armazena_dados_cliente(self, documento)

        # Define o foco em um QLineEdit com 'doc' em seu nome
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QLineEdit) and 'doc' in widget.objectName():
                widget.setFocus()
                break




