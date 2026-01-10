"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

def discount_calculator(preco, percentual_desconto):
    valor_desconto = preco * percentual_desconto
    total_com_desconto = preco - valor_desconto
    return total_com_desconto

def show_details(nome_produto, valor_original, taxa, valor_final):
    print(f"Produto: {nome_produto}")
    print(f"Preço Original: R${valor_original:.2f}")
    print(f"Desconto: {taxa * 100}%")
    print(f"Preço Final: R${valor_final:.2f}")
    
TAXA_DESCONTO = 0.20

print("----- Calculadora de Desconto -----")
print("Escolha um produto:")
print("1 - Camiseta")
print("2 - Calça")
print("3 - Meia")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    produto = "Camiseta"
    preco_original = 50.00
    preco_final = discount_calculator(preco_original, TAXA_DESCONTO)
    show_details(produto, preco_original, TAXA_DESCONTO, preco_final)
elif opcao == 2:
    produto = "Calça"
    preco_original = 80.00
    preco_final = discount_calculator(preco_original, TAXA_DESCONTO)
    show_details(produto, preco_original, TAXA_DESCONTO, preco_final)
elif opcao == 3:
    produto = "Meia"
    preco_original = 10.00
    preco_final = discount_calculator(preco_original, TAXA_DESCONTO)
    show_details(produto, preco_original, TAXA_DESCONTO, preco_final)
else:
    print("Opção inválida. Tente novamente.")