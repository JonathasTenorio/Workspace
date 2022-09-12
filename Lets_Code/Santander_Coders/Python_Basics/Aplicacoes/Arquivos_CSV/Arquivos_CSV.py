import csv

with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    header = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

with open('users_csv.csv', 'w', encoding='utf-8', newline='') as users:
    escritor = csv.writer(users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Pietro', 'Ribeiro', 'Pietro@gmail.com', 'Masculino'])

with open('users_csv.csv', 'r', encoding='utf-8') as usuarios:
    reader = csv.reader(usuarios)
    for linha in reader:
        print(linha)