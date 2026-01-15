"""Crie uma função que verifique se uma palavra ou frase é um
palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for
False, responda “Não” """

def verificar_palindromo(frase):
    frase = frase.lower().replace(" ", "")
    frase_invertida = frase[::-1]
    return frase == frase_invertida

entrada = input("Digite uma palavra ou frase: ")
if verificar_palindromo(entrada):
    print("Sim")
else:
    print("Não")