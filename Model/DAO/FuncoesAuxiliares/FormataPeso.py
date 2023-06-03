def formata_peso(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 5:
        # Limita o tamanho do texto
        text = text[:5]

    formatted_text = ''
    for i in range(len(text)):
        if i == 2:
            formatted_text += '.'
        formatted_text += text[i]

    return formatted_text


