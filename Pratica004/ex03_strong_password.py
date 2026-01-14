"""Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'."""

def senha_forte(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        break
    if senha_forte(senha):
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Tente novamente.")
print("Programa encerrado.")