"""Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
"""

print("Este programa irá ler um valor e mostrar se ele está entre [0,25]; (25,50]; (50,75]; (75,100]")
valor = float(input("Digite um valor entre 0 e 100. \n"))

if 0 <= valor <= 25:
    print("O valor está contido entre 0 e 25.")
elif 25 < valor <= 50:
    print("O valor está contido entre 25 e 50.")
elif 50 < valor <= 75:
    print("O valor está contido entre 50 e 75.")
elif 75 < valor <= 100:
    print("O valor está contido entre 75 e 100.")
else:
    print("Fora de intervalo")
