def formata_real(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 6:
        # Limita o tamanho do texto
        text = text[:6]

    num_digits = len(text)

    if num_digits <= 2:
        return text

    formatted_text = text[:-2] + ',' + text[-2:]

    if num_digits > 3:
        thousands = formatted_text[:-6]
        if thousands:
            formatted_text = thousands + '.' + formatted_text[-6:]

    return formatted_text


