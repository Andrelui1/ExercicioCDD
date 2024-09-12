numeroAlunos = int(input("Digite a quantidade de alunos: "))
soma = 0
for x in range(1, numeroAlunos+1):
    notas = float(input(f"Digite a nota do aluno {x}: "))
    soma = soma + notas

    media = soma / numeroAlunos

print(media)
