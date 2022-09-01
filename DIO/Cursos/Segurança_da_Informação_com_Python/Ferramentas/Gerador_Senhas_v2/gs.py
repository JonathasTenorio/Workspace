import random, string

size = 3

chars = string.ascii_letters + string.digits + '!@#$%¨&*()-_=+§ªº/?°;:.>,<'

string = input("Digite uma string\n")

rand = random.SystemRandom()

with open("a.txt", "r", encoding="UTF-8") as file:

	for linha in file:
		linhas = linha.strip()
	#	print(linhas)
		if (string == linhas):
			print("É igual: " + string + " A string do arquivo é: " + linhas )
			break
		else:
			print(linhas)



'''if ('izi' in fread):
	print(True)
else:
	print(False)
#print(''.join(rand.choice(chars) for i in range(size)))
'''
