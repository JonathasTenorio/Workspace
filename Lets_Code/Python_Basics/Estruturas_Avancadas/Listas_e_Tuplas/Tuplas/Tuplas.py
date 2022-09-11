print('Criando tuplas com python!')
print('Exemplo: tupla = "string1", "string2"   ou    tupla = ("string1", "string2")')
nome_paises = 'Brasil', 'Argentina', 'China', 'Canada', 'Japao'
print('A tupla criada contem os seguintes elementos: ', nome_paises, '\n')
print('Utilizando unpacking com tupla')
a, b, c, de, f = nome_paises
print(a, b, c, '\n')
print(*nome_paises)
