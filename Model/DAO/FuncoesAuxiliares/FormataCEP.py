def formata_cep(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 8:
        # Limita o tamanho do texto
        text = text[:8]

    formatted_text = ''
    for i in range(len(text)):
        if i == 5:
            formatted_text += '-'
        formatted_text += text[i]
    return formatted_text
