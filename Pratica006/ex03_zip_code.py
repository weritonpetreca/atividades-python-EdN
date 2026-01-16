"""Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado."""

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['logradouro'], dados['bairro'], dados['localidade'], dados['uf']
    else:
        raise Exception("Erro ao consultar o CEP.")

try:
    cep = input("Digite um CEP: ")
    logradouro, bairro, cidade, estado = consultar_cep(cep)
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
except Exception as e:
    print("Erro:", e)