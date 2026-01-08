"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

produto = "Cadeira Infantil"
preco = 12.4
quantidade = 3

total = preco * quantidade

print("O total a pagar por " + str(quantidade) + " unidades da " + produto + " é de R$" + str(total))