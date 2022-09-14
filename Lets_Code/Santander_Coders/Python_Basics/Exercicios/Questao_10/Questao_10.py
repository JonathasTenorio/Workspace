tru = True
while tru:
    print("""\nEste programa irá verificar se a composição possui a compassagem correta.
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
    composicao = composicao.split('/')

    for element in range(len(composicao)):
        if '' == composicao[element-1]:
            composicao.remove('')
    errors = []
    acertos = 0
    for element in composicao:
        somador = 0
        for note in element:
            if somador > 1:
                break
            else:
                for key in notas:
                    if note == key:
                        somador = somador + notas[key]
                        break
        if somador != 1:
            errors.append(element)
        else:
            acertos = acertos + 1

    print(f'Qtd. de Corretos: {acertos}')
    print(f'Incorretos: {errors}')
    slc = '0'
    while slc != '1' or slc != '2':
        slc = str(input("""Deseja realizar uma nova consulta ?
        1) -- SIM
        2) -- NÃO
        """))
        if slc == '2':
            tru = False
            break
        else:
            break
