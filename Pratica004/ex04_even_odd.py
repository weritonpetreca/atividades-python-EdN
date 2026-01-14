"""Crie um programa que solicite ao usuário que insira números
inteiros. O programa deve continuar solicitando números até
que o usuário digite 'fim'. Para cada número inserido, o
programa deve informar se é par ou ímpar. Se o usuário
inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a
quantidade de números pares e ímpares inseridos."""

pares = 0
impares = 0
while True:
    numero = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if numero.lower() == 'fim':
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            pares += 1
            print(f"{numero} é par.")
        else:
            impares += 1
            print(f"{numero} é ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print("Programa encerrado.")