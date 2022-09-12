#arquivo = open('../DomCasmurro.txt', 'r', encoding='utf-8')
"""texto = arquivo.read()
print(texto)
"""

#linha = arquivo.readline()
"""
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()
"""

#for linha in arquivo:
#   print(linha, end='')
#arquivo.close()

with open('DomCasmurro.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)


with open('arquivo_teste.txt', 'w', encoding='utf-8') as file:
    file.write('Essa é uma linha que eu escrevi usando Python.\n')
    file.write('Segunda linha usando Python.\n')

with open('arquivo_teste.txt', 'a', encoding='utf-8') as zfile:
    zfile.write('Terceira linha escrita usando Python.\n')

with open('arquivo_teste.txt', 'r', encoding='utf-8') as file:
    print(file.read())