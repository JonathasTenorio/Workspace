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

composicao = str.upper(input("Insira a composição\n"))
print(composicao) #Apagar depois
composicao = composicao.split('/')
print(composicao) #Apagar Depois

for element in range(len(composicao)): #Rever posteriormente, provável erro de lógica entre iteração e método.
    if '' == composicao[element-1]:
        composicao.remove('')
print(composicao) # Apagar depois
somador = 0
counter = 0
errors = []
acertos = 0
#while counter < len(composicao):
for element in composicao:
    if somador < 1:
        print(f'Estamos no elemento: {element}')
        for note in element:
            print(f'Esta é a nota: {note} do elemento {element}')
            for key in notas:
                print(f'Esta é a chave: {key}')
                if note == key:
                    print('Igual')
                    somador = somador + notas[key]
                    break
                #else:
print(somador)