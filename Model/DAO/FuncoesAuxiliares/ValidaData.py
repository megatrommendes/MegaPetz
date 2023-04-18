from datetime import datetime


def valida_data(text):
    # Verifica se a data está no formato correto (DD/MM/AAAA)
    try:
        datetime.strptime(text, '%d/%m/%Y')
        return True
    except ValueError:
        return False
