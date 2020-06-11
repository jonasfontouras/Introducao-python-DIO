import pip._vendor.requests

def retorna_dados_cep(cep):
    response = pip._vendor.requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    print(dados_cep['cep'])
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    print(dados_cep['bairro'])
    print(dados_cep['localidade'])
    print(dados_cep['uf'])
    print(dados_cep['unidade'])
    print(dados_cep['ibge'])
    return dados_cep

if  __name__ == "__main__":
    inputcep = str(input('Degite seu CEP: '))
    retorna_dados_cep('{}'.format(inputcep))