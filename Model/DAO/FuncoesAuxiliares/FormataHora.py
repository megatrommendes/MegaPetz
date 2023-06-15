def formata_hora(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 4:
        # Limita o tamanho do texto
        text = text[:4]

    formatted_text = ''
    for i in range(len(text)):
        if i == 2:
            formatted_text += ':'
        formatted_text += text[i]

    if len(formatted_text) >= 5:
        if "00:0" in formatted_text:
            return formatted_text + "s"

        elif "00:" in formatted_text:
            return formatted_text + "min"
        else:
            return formatted_text + "h"
    else:
        return formatted_text
