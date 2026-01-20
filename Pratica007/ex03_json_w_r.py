"""3- Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo.
Para isso:

 * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
 * Solicite ao usuário o nome do arquivo JSON.
* Salve os dados no arquivo usando o módulo `json`.
 * Após salvar, leia o mesmo arquivo e imprima os dados carregados.
 * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

 Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo."""
 
import json

def main():
    dados_pessoa = {
        'nome': input("Digite o nome: "),
        'idade': input("Digite a idade: "),
        'cidade': input("Digite a cidade: ")
    }

    nome_arquivo = input("Digite o nome do arquivo JSON para salvar os dados: ")
    if not nome_arquivo.lower().endswith('.json'):
        nome_arquivo += '.json'
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_pessoa, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos em {nome_arquivo}")
    except IOError:
        print("Ocorreu um erro ao tentar escrever no arquivo.")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_lidos = json.load(arquivo_json)
        print(f"Dados lidos do arquivo {nome_arquivo}:")
        print(dados_lidos)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"O arquivo '{nome_arquivo}' não está no formato JSON válido.")
        
if __name__ == "__main__":
    main()