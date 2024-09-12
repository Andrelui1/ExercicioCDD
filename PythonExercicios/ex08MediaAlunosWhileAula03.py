alunos = int(input("Digite a quantodade de alunos: "))
contador = 1
soma = 0
while contador <= alunos:
    notas = int(input(f"Digite as notas do aluno {contador}: "))
    contador += 1
    soma = soma + notas

media = soma / alunos
print(f"a soma é: {soma} e a media é: {media}")
