import requests
cep_input = input('Digite o CEP')
if len(cep_input) != 8:
    print('Digitos inválidos')
    exit()

    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))
    print(request.json())
