def hello():
    print('Hello World')
hello()

def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(3,6,9)

print(resultado)

resultado2 = calcula_media(valor1= 4, valor2=5, valor3=12)

print(resultado2)

resultado3 = calcula_media()

print(resultado3)