"""Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória."""

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

try:
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    senha_gerada = gerar_senha(tamanho_senha)
    print("Senha gerada:", senha_gerada)
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")