from PyQt5.QtWidgets import QWidget, QLineEdit

from Model.DAO.FuncoesFormularios.FuncoesFormCliente.ValidaDadosCliente import valida_dados_cliente
from Model.DAO.FuncoesFormularios.FuncoesFormCliente.ArmazenaDadosCliente import armazena_dados_cliente


def validar_salvar_cliente(self):
    ok, documento = valida_dados_cliente(self)
    if ok:
        armazena_dados_cliente(self, documento)
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QLineEdit) and 'doc' in widget.objectName():
                widget.setFocus()
                break



