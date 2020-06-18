import requests
print()
def CEP(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(CEP))
    print('STATUS: {}'.format(response.status_code))
    print()
    print('INFORMAÇÂO: {}'.format(response.text))
    print()
    #Selecionando informações dentro do REQUEST
    dados_cep = response.json()
    print('CEP: {}'.format(dados_cep['cep']))
    print('LOGRADOURO: {}'.format(dados_cep['logradouro']))
    print('BAIRRO: {}'.format(dados_cep['bairro']))
    print('LOCALIDADE: {}'.format(dados_cep['localidade']))
    print('UF: {}'.format(dados_cep['uf']))
    print('IBGE: {}'.format(dados_cep['ibge']))
    return cep

def pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    pokemon_dados = response.json()
    return  pokemon_dados

if __name__ == ' __main__ ':
    CEP('71693009')
    pokemon_dados = pokemon('pikachu')
    print(pokemon_dados)
