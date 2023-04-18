import requests

from Model.DAO.FuncoesAuxiliares.EnviaMensagem import envia_mensagem


def consulta_cep_correio(cep):
    # URL da API do ViaCEP para consulta de CEP
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # faz uma solicitação GET para a API do ViaCEP
    response = requests.get(url)

    if response.ok:
        # extrai os dados do endereço do JSON
        endereco = response.json()
        if "erro" in endereco and endereco["erro"] == True:
            envia_mensagem("Erro de validação.", "CEP não localizado.")
            return '', '', '', ''
        else:
            logradouro = endereco.get('logradouro', '')
            if logradouro == '':
                envia_mensagem("Erro de validação.", "CEP não localizado.")
                return '', '', '', ''
            else:
                logradouro = endereco.get('logradouro', '')
                bairro = endereco.get('bairro', '')
                localidade = endereco.get('localidade', '')
                uf = endereco.get('uf', '')
                return logradouro, bairro, localidade, uf
    else:
        envia_mensagem("Erro de validação.", "CEP não localizado.")
        return '', '', '', ''
