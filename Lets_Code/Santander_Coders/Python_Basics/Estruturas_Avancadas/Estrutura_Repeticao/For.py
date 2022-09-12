nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'París']

for nome in nomes_cidades:
    print(nome)

dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes': 12.2
}

for chave in dados_cidade:
    print(f'{chave}: {dados_cidade[chave]}')


for posicao in range (len(nomes_cidades)):
    nomes_cidades[posicao] = 'Rio de Janeiro'

print(nomes_cidades)