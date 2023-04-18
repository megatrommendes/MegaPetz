def so_numero(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))
    return text
