frase = "O professor Pietro da Let's Code disse : \"Hoje a pizza é por minha conta.\""
print(frase)


empresa = 'Google'
print("Exemplo índices e strings\nAcessando a string na posição[0].")
print(empresa[0])
print("Acessando a string até a posição [3].")
print(empresa[:3])

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"


print("\nexemplo do métodos split.\n")
print("Criando variável com a string: " + nomes_cidades)
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)


print("\n Exemplo do método strip")
cabecalho = "           menu                "
print(cabecalho)
print(cabecalho.strip())


print("\n Exemplo de métodos de string\n")
nome_cidade = 'rIo DE jaNeirO'


print("Método title: "+ nome_cidade.title())
print("Método capitalize: "+ nome_cidade.capitalize())
print("Método lower: "+ nome_cidade.lower())
print("Método upper "+ nome_cidade.upper())


print("\nUtilizando o método 'in' em strings")
mensagem = "Você viu o que o Pietro disse na sala ontem ?"
print(mensagem)
fui_citado = 'Pietro' in mensagem
print(fui_citado)