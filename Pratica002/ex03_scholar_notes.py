"""3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

def calcular_media(lista_notas):
    soma = sum(lista_notas)
    media_calculada = soma / len(lista_notas)
    return media_calculada

def mostrar_detalhes(lista_notas, valor_media):
    for indice, valor_nota in enumerate(lista_notas, start=1):
        print(f"Nota {indice}: {valor_nota:.2f}")
    print(f"Média Final: {valor_media:.2f}")
    
print("----- Calculadora de Média Escolar -----")
print("Digite as notas do aluno:")
notas = []
for i in range(3):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)

media = calcular_media(notas)
mostrar_detalhes(notas, media)