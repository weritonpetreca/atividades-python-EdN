"""1- Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
Para isso:

 * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
 * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
 * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
 * Confirme a gravação exibindo uma mensagem com o nome do arquivo.
 * Trate possíveis erros de escrita de arquivo.

 Dica: Use `csv.writer()` para escrever os dados linha por linha."""
 
import csv

def main():
    dados = []
    for i in range(3):
        nome = input(f"Digite o nome da pessoa {i+1}: ")
        idade = input(f"Digite a idade da pessoa {i+1}: ")
        cidade = input(f"Digite a cidade da pessoa {i+1}: ")
        dados.append([nome, idade, cidade])

    nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados: ")
    if not nome_arquivo.lower().endswith('.csv'):
        nome_arquivo += '.csv'
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])  # Cabeçalhos
            escritor_csv.writerows(dados)
        print(f"Dados salvos em {nome_arquivo}")
    except IOError:
        print("Ocorreu um erro ao tentar escrever no arquivo.")

if __name__ == "__main__":
    main()