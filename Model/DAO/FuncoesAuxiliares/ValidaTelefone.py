from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


def valida_telefone(text):
    # Verifica se o campo de telefone possui a quantidade de digitos do número do telefone
    if len(text) == 14:
        return True
    else:
        envia_mensagem("Erro de validação", "Número de telefone incorreto.")
        return False
