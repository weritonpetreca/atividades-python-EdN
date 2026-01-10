"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
print("----- Conversor de Moeda -----")
print("Escolha uma opção:")
print("1 - Real para Dólar")
print("2 - Real para Euro")
print("3 - Dólar para Real")
print("4 - Euro para Real")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    valor_reais = float(input("Digite o valor em reais (R$): "))
    taxa_dolar = 5.20
    valor_dolar = valor_reais / taxa_dolar
    print(f"Valor em Dólar: ${valor_dolar:.2f}")
elif opcao == 2:
    valor_reais = float(input("Digite o valor em reais (R$): "))
    taxa_euro = 6.15
    valor_euro = valor_reais / taxa_euro
    print(f"Valor em Euro: €{valor_euro:.2f}")
elif opcao == 3:
    valor_dolar = float(input("Digite o valor em Dólar ($): "))
    taxa_dolar = 5.20
    valor_reais = valor_dolar * taxa_dolar
    print(f"Valor em Reais: R${valor_reais:.2f}")
elif opcao == 4:
    valor_euro = float(input("Digite o valor em Euro (€): "))
    taxa_euro = 6.15
    valor_reais = valor_euro * taxa_euro
    print(f"Valor em Reais: R${valor_reais:.2f}")
else:
    print("Opção inválida. Tente novamente.")