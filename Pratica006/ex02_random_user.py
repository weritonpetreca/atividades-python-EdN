"""Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado."""

import requests

def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url, timeout=10)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        
        name = f"{usuario['name']['first']} {usuario['name']['last']}"
        e_mail = usuario['email']
        country = usuario['location']['country']
        return name, e_mail, country
    else:
        raise Exception("Erro ao acessar a API de usuário aleatório.")
    
try:
    nome, email, pais = gerar_usuario_aleatorio()
    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)
except Exception as e:
    print("Erro:", e)