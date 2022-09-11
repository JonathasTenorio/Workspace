print('Criando listas com Python!\n')
print('Exemplo: lista = ["string1", "string2", "string3"]')
nome_paises = ['Brasil', 'Argentina', 'China', 'Canada', 'Japao']
print('A lista criada contem os seguintes elementos: ', nome_paises)
print('Tamanho da lista: ', len(nome_paises), '\n')

print('Acessando índices fixos de uma lista.\n')
print('lista[4]')
print('País: ', nome_paises[4], '\n')

print('Acessando índice negativo em uma lista.\n')
print('lista[-1]')
print('País: ', nome_paises[-1], '\n')

print('Trocando o valor do índice [4].')
nome_paises[4] = 'Colômbia'
print('País: ', nome_paises[4])
print(nome_paises)

print('Exemplo de percorrer listas partindo do índice 1 até o 3 [1:3]. ',nome_paises[1:3])
print('Exemplo de percorrer listas indo até índices negativos [1:-1]. ', nome_paises[1:-1])
print('Exemplo de percorrer listas partindo do índice 2 da lista [2:]. ',nome_paises[2:])
print('Exemplo de percorrer listas até o índice 3 das lista [:3]. ', nome_paises[:3])
print('Exemplo de percorrer listas com Slicing(fatiamento) sem  definir inicio e fim [:]. ', nome_paises[:])
print('Exemplo de percorrer listas com salto(step) entre índices [::2]. ', nome_paises[::2], '\n')

print('Utilizando a função "in" do python.')
print('Exemplo: Brasil in lista')
print('Brasil' in nome_paises, '\n')


print('Utilizando a função "not in" do python.')
print('Exemplo: Canada in lista')
print('Canada' in nome_paises, '\n')

print('Criando lista vazia.')
print('Exemplo: lista = [] \n')
lista_captais = []

print('Utilizando método append para adicionar elementos ao final da lista.')
print('Exemplo: lista.append("string1")')
lista_captais.append('Brasília')
lista_captais.append('Buenos Aires')
lista_captais.append('Pequim')
lista_captais.append('Bogotá')
print(lista_captais, '\n')

print('Utilizando método insert para inserir elementos na lista')
print('Exemplo: lista.insert(índice, "elemento")')
lista_captais.insert(2, 'París')
print(lista_captais, '\n')


print('Utilizando método remove para deletar elementos da lista')
print('Exemplo: lista.remove("elemento")')
lista_captais.remove('Buenos Aires')
print(lista_captais, '\n')


print('Utilizando método pop para remover elementos na lista')
print('Exemplo: lista.pop(índice)')
removidos = lista_captais.pop(2)
print(lista_captais, removidos,'\n')


