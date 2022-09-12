idade = input("Informe a sua idade")
print(idade, type(idade))

idade = int(idade)
print(idade, type(idade))

print(float('123.25'))
print(str('123.25'))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-2))


salario_mensal = input("Digite o valor do seu salario mensal: ")
salario_mensal = float(salario_mensal)

gasto_mensal = input("Digite o valor do seu gasto mensal em media: ")
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total

print("O montante que você pode economizar no fim do ano é de ", montante_economizado)
