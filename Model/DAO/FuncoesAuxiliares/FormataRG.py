def formata_rg(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))
    if len(text) > 14:
        # Limita o tamanho do texto
        text = text[:14]
    formatted_text = ''
    for i in range(len(text)):
        if i == 2:
            formatted_text += '.' + text[i]
        elif i == 5:
            formatted_text += '.' + text[i]
        elif i == 8:
            formatted_text += '-' + text[i]
        else:
            formatted_text += text[i]
    return formatted_text
