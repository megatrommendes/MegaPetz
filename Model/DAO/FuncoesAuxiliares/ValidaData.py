from datetime import datetime

from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


def valida_data(self, text):
    # Verifica se a data está no formato correto (DD/MM/AAAA)
    try:
        datetime.strptime(text, '%d/%m/%Y')
        return True
    except ValueError:
        envia_mensagem("Erro de validação", "Data incorreta.")
        self.focusWidget()
        return False
