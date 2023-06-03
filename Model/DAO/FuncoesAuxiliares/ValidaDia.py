def valida_dia(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    # Verifica se o número está entre 1 e 31
    if text.isdigit():
        num = int(text)
        if 1 <= num <= 31:
            return text

    return ''
