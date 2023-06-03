from datetime import datetime

from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem

from datetime import datetime, date


def valida_data(self, text):
    # Verifica se a data está no formato correto (DD/MM/AAAA)
    try:
        data = datetime.strptime(text, '%d/%m/%Y').date()
        data_atual = date.today()

        if data > data_atual:
            envia_mensagem("Erro de validação", "Data maior que a data atual.")
            self.focusWidget()
            return False

        return True
    except ValueError:
        envia_mensagem("Erro de validação", "Data incorreta.")
        self.focusWidget()
        return False

