from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


def valida_texto(text):
    if text == '':
        envia_mensagem("Erro de validação", "Esse campo é obrigatório.")
        return False
    else:
        return True
