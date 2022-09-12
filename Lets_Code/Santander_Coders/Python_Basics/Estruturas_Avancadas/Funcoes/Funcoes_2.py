def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem

print(calcula_media(3, 4, 20, margem=0.3))

def sum(valor):
    soma = 0
    for i in range (len(valor)):
        soma = soma + valor[i]
        return soma


def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Pietro', sobrenome='Ribeiro')