"""Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento."""

def calcular_idade_em_dias(ano_nascimento, mes_nascimento, dia_nascimento, ano_atual, mes_atual, dia_atual):
    # Calcular anos, meses e dias
    years = ano_atual - ano_nascimento
    months = mes_atual - mes_nascimento
    days = dia_atual - dia_nascimento
    # Ajustar meses e anos se necessário
    if days < 0:
        months -= 1
        days += 30  # Aproximação simples, não considerando meses com 28, 29 ou 31 dias

    if months < 0:
        years -= 1
        months += 12

    # Calcular total de dias
    total_days = years * 365 + months * 30 + days
    return total_days

print("----- Calculadora de Idade em Dias -----")

try:
    birth_year = int(input("Digite o ano de nascimento: "))
    birth_month = int(input("Digite o mês de nascimento (1-12): "))
    birth_day = int(input("Digite o dia de nascimento: "))
    current_year = int(input("Digite o ano atual: "))
    current_month = int(input("Digite o mês atual (1-12): "))
    current_day = int(input("Digite o dia atual: "))
except ValueError:
    print("Entrada inválida. Por favor, insira números inteiros válidos.")
    exit()
days_of_life = calcular_idade_em_dias(birth_year, birth_month, birth_day, current_year, current_month, current_day)
print(f"A idade em dias é: {days_of_life} dias")