"""Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'."""

def verificar_senha_forte(senha):
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        return True
    else:
        return False

while True:
    password = input("Digite uma senha (ou 'sair' para sair): ")
    if password.lower() == 'sair':
        print("Programa encerrado.")
        break
    if verificar_senha_forte(password):
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Tente novamente.")