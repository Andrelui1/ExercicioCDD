notas = [""] * 5
cont = 0
soma = 0
tamanho = len(notas)

for i in range(tamanho):
    notas[i] = float(input("Digite sua nota: "))

for x in range(tamanho):
   soma += notas[x]
media = soma/tamanho

for z in range(tamanho):
    if notas[z] > media:
        cont = cont+1
print(f"A media da turma e {media} e "
      f"{cont} alunos tiveram nota maior que a media")

