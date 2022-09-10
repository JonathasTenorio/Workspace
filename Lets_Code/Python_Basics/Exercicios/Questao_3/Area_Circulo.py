import math
"""
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
"""


print("Este programa irá calcular a área de um círculo dado o raio.")
r = float(input("Digite o valor do raio: \n"))

area = math.pi * (math.pow(r, 2))

print('A área do circulo é {}'.format(area))

