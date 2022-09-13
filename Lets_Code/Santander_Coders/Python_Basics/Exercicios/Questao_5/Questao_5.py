print("""Este programa irá descobrir o assassino de um crime.
Só pode responder com Sim(Y/y) ou Não(N/n)
""")

pts = 0

txt = str.lower(input("Mora perto da vítima?\nSim(Y/y)  Não(N/n)"))
if 'y' in txt:
    pts = pts + 1
txt = str.lower(input("Já trabalhou com a vítima?\nSim(Y/y)  Não(N/n)"))
if 'y' in txt:
    pts = pts + 1
txt = str.lower(input("Telefonou para a vítima?\nSim(Y/y)  Não(N/n)"))
if 'y' in txt:
    pts = pts + 1
txt = str.lower(input("Esteve no local do crime?\nSim(Y/y)  Não(N/n)"))
if 'y' in txt:
    pts = pts + 1
txt = str.lower(input("Devia para a vítima?\nSim(Y/y)  Não(N/n)"))
if 'y' in txt:
    pts = pts + 1

print(pts)

if pts < 5:
    if pts < 3:
        if pts > 1:
            print("Você é um suspeito!")
        else:
            print("Você está liberado.")
    else:
        print("Você está preso por ser cúmplice!")
else:
    print("Você está preso por assassinato!")