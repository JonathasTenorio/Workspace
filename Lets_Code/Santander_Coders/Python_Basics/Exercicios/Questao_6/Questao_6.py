def soma_list(valor):
    sum = 0
    for i in range(len(valor)):
        sum = valor[i] + sum
    return sum

print(soma_list([3, 5, 6, 98]))