"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""

def calcular_consumo(distancia, combustivel):
    consumo_medio = distancia / combustivel
    return consumo_medio

def mostrar_detalhes(distancia, combustivel, consumo):
    print(f"Distância Percorrida: {distancia} km")
    print(f"Combustível Gasto: {combustivel} litros")
    print(f"Consumo Médio: {consumo:.2f} km/l") 

print("----- Calculadora de Consumo de Combustível -----")
distancia_percorrida = float(input("Digite a distância percorrida (km): "))
combustivel_gasto = float(input("Digite o combustível gasto (litros): "))

consumo_medio_carro = calcular_consumo(distancia_percorrida, combustivel_gasto)
mostrar_detalhes(distancia_percorrida, combustivel_gasto, consumo_medio_carro)