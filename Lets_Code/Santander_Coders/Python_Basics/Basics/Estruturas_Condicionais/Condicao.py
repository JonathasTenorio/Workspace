valor_passagem = 4.30

valor_corrida = input("Qual é o valor da corrida?")

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
elif float(valor_corrida) <= valor_passagem * 6:
    print("Aguarde um momento, o valor pode abaixar")
else:
    print('Pegue o ônibus')
