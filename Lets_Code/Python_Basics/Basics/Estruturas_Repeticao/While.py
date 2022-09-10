Counter = 0

while Counter < 10:
    Counter += 1
    if Counter == 1:
        print(Counter, "Item limpo")
    else:
        print(Counter, "Items limpos")

print("Fim do while")

Counter = 0

while True:
    if Counter < 10:
        Counter += 1
        if Counter == 1:
            print(Counter, "Item limpo")
        else:
            print(Counter, "Items limpos")
    else:
        break

print("Fim do while")

texto = input("Digite uma senha: ")

while texto != "Let'sCode":
    texto=input("Senha inválida. Tente novamente")

print("Acesso permitido")


Counter = 0

while True:
    if Counter < 10:
        Counter += 1
        if Counter == 1:
            continue
        print(Counter, "Items limpos")
    else:
        break

print("Fim do while")
