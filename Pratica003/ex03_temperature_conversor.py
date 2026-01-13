"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

try:
    temperatura = float(input("Digite a temperatura a ser convertida: "))
except ValueError:
    print("Erro: A temperatura deve ser um número válido.")
    exit()

unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
if unidade_origem not in ["C", "F", "K"]:
    print("Erro: Unidade de origem inválida. Escolha C, F ou K.")
    exit()

unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()
if unidade_destino not in ["C", "F", "K"]:
    print("Erro: Unidade de destino inválida. Escolha C, F ou K.")
    exit()

resultado = None

if unidade_origem == "C":
    if unidade_destino == "F":
        resultado = celsius_to_fahrenheit(temperatura)
    elif unidade_destino == "K":
        resultado = celsius_to_kelvin(temperatura)
    else:
        print("Unidade de destino inválida.")
elif unidade_origem == "F":
    if unidade_destino == "C":
        resultado = fahrenheit_to_celsius(temperatura)
    elif unidade_destino == "K":
        resultado = fahrenheit_to_kelvin(temperatura)
    else:
        print("Unidade de destino inválida.")
elif unidade_origem == "K":
    if unidade_destino == "C":
        resultado = kelvin_to_celsius(temperatura)
    elif unidade_destino == "F":
        resultado = kelvin_to_fahrenheit(temperatura)
    else:
        print("Unidade de destino inválida.")
else:
    print("Unidade de origem inválida.")

if resultado is not None:
    print(f"{temperatura} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}.")
else:
    print("Operação inválida.")
    exit()