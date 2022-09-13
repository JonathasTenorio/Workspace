print("""Este programa irá verificar se a composição possui a compassagem correta.
    Exemplo de input: /W/HH/QQQQ/
    """)
notas = {
        'W': 1,
        'H': 1/2,
        'Q': 1/4,
        'E': 1/8,
        'S': 1/16,
        'T': 1/32,
        'X': 1/64
        }

composicao = str.upper(input("Insira a composição"))
print(composicao)
print(notas)
n = 0
for key in notas:
    print(n)
    if key in composicao: