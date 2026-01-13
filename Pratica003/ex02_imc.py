"""2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso" """

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

try:
    altura = float(altura)
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")
except ValueError as e:
    print(f"Erro: {e}")
    exit()

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc >= 30:
    classificacao = "Obeso"
else:
    classificacao = "Valor de IMC inválido"

print(f"Seu IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")