from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


def valida_real(text):
    # Remove caracteres não numéricos, exceto a vírgula
    text = ''.join(filter(lambda x: x.isdigit() or x == ',', text))

    # Verifica se a string tem menos de 4 dígitos ou contém a sequência '0,' em qualquer parte
    if len(text) <= 2:
        envia_mensagem("Erro de validação", "Valor incorreto.")
        return False
    else:
        return True
