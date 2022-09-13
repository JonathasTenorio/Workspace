arm = []
for i in range(3):
    if i < 2:
        valor = float(input("Digite um número inteiro."))
    else:
        valor = float(input("Digite um número real"))
    arm.append(valor)

print((arm[0]*2)*(arm[1]/2))
print((arm[0]*3)+arm[2])
print(arm[2]**3)