from datetime import datetime, date


def calcular_diferenca_data(data):
    try:
        data_obj = datetime.strptime(data, '%d/%m/%Y').date()
    except ValueError:
        return False

    data_atual = date.today()

    if data_obj > data_atual:
        return False

    diferenca = data_atual - data_obj

    if diferenca.days == 0:
        return 0, 'Dia(s)'

    if diferenca.days > 365:
        anos = diferenca.days // 365
        return anos, 'Ano(s)'

    if diferenca.days > 30:
        meses = diferenca.days // 30
        return meses, 'Mês(s)'

    return diferenca.days, 'Dia(s)'
