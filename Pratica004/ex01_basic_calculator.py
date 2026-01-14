"""Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição,
subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com
diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja
concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa."""

def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
        return n1 / n2
    else:
        raise AttributeError("Erro: Operação inválida. Use +, -, * ou /.")
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida (não numérica).")
        continue

    try:
        operacao = input("Digite a operação (+, -, *, /): ")
        resultado = calcular(num1, num2, operacao)
    except AttributeError as ae:
        print(ae)
        continue
    except ZeroDivisionError as zde:
        print(zde)
        continue

    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
    break

print("Calculadora encerrada.")