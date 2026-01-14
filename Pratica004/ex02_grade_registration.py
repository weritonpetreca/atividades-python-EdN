"""Crie um programa que permita a um professor registrar as
notas de uma turma. O programa deve continuar solicitando
notas até que o professor digite 'fim'. Notas válidas são de 0 a
10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma."""

notas = []
while True:
    nota = input("Digite a nota (ou 'fim' para encerrar): ")
    if nota.lower() == 'fim':
        break
    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

media = sum(notas) / len(notas) if notas else 0
print(f"A média da turma é: {media:.2f}, foram registradas {len(notas)} notas.")