import math
i = 0
soma = 0
max = 1000
while i < max:
    soma = soma + 1/math.factorial(max - i)
    i += 1

print(soma)