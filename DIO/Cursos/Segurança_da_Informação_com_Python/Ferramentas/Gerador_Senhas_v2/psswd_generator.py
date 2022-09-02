import random
import string
import sys
import argparse

alpha = string.ascii_letters
num = string.digits
espc = '! @#$%¨&*()-_=+§ªº/?°;:.>,<'
parser = argparse.ArgumentParser(description="GERADOR DE SENHAS RANDOMICAS!")
parser.add_argument('-s', '--size', type=int, help='Quantidade de caracteres que tera a senha gerada.', default=8)
parser.add_argument('-a', '--alpha', help='Utiliza apenas letras para gerar a senha.', default=alpha)
parser.add_argument('-f', '--file', help='Nome da wordlist\nSe nao especificado ira utilizar a rockyou.txt no diretorio atual.\nA wordlist precisa estar no diretório atual.', default='rockyou.txt')
args = parser.parse_args()

def gerador(chars, size, path):
	rand = random.SystemRandom()
	jst = (''.join(rand.choice(chars) for _ in range(size)))
	print('A senha gerada foi: {}'.format(jst))
	with open(path, "r", encoding="ISO-8859-1") as file:
		print("Buscando senha igual à gerada . . . . .")
		for linha in file:
			linhas = linha.strip()
			if jst == linhas:
				return print("É igual: " + jst + " A string do arquivo é: " + linhas)
				break

	print("Sucesso! A sua senha não é igual a nenhuma outra neste arquivo.")


if __name__ == '__main__':
	'''
	======================================
	|| Gerador e Comparador de Senhas 	||
	|| version 2.0						||
	||									||
	|| gs.py -a 'abcde' -s 4			||
	======================================
	
	'''
	gerador(args.alpha, args.size,args.file)