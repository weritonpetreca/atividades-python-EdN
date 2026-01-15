"""Crie uma função que calcule a gorjeta a ser deixada em
um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada.
 Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
 Parâmetros:
 valor_conta (float): O valor total da conta
 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
 Retorna: float: O valor da gorjeta calculada"""
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = (porcentagem_gorjeta / 100) * valor_conta
    return gorjeta

print("----- Calculadora de Gorjeta -----")
try:
    bill_value = float(input("Digite o valor total da conta: R$ "))
    tip_percentage = float(input("Digite a porcentagem de gorjeta desejada: "))
    if bill_value < 0 or tip_percentage < 0:
        print("Por favor, insira valores positivos.")
        exit()
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
    exit()
valor_gorjeta = calcular_gorjeta(bill_value, tip_percentage)
print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")