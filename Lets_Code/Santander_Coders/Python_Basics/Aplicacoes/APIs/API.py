"""
É necessário instalar a biblioteca requests

Ex.: pip install requests

"""
import requests
url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)
dados = req.json()

valor_reais = float(input('Informe o valor em R$(Reais) a ser convertido: \n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem U$ {(valor_reais/ cotacao):.2f}')

