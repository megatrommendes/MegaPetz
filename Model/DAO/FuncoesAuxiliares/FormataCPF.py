def formata_cpf(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))
    if len(text) > 14:
        # Limita o tamanho do texto
        text = text[:14]
    formatted_text = ''
    for i in range(len(text)):
        if i == 3:
            formatted_text += '.' + text[i]
        elif i == 6:
            formatted_text += '.' + text[i]
        elif i == 9:
            formatted_text += '-' + text[i]
        else:
            formatted_text += text[i]
    return formatted_text
