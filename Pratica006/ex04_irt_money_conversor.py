"""Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação."""

import requests

def consultar_cotacao(coin):
    url = f"https://economia.awesomeapi.com.br/json/last/{coin}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        conversion = dados[f"{coin}BRL"]["name"]
        cotation = dados[f"{coin}BRL"]["bid"]
        minimun = dados[f"{coin}BRL"]["low"]
        maximun = dados[f"{coin}BRL"]["high"]
        date_time = dados[f"{coin}BRL"]["create_date"]
        return conversion, cotation, minimun, maximun, date_time
    else:
        raise Exception("Erro ao consultar a cotação.")
    
try:
    moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
    conversion, cotation, minimun, maximun, date_time = consultar_cotacao(moeda)
    print(f"Conversão de {moeda}: {conversion}")
    print(f"Cotação atual de {moeda}: {cotation}")
    print(f"Cotação mínima de {moeda}: {minimun}")
    print(f"Cotação máxima de {moeda}: {maximun}")
    print(f"Data e hora da última atualização: {date_time}")
except Exception as e:
    print("Erro:", e)