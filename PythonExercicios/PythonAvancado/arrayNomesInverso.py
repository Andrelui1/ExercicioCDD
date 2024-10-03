nomes = [""]*5
tamanho = len(nomes)
for x in range(tamanho):
    nomes[x] = input("Digite um nome: ")
print(nomes)
"""for i in range(4, -1, - 1):
    print(nomes[i], end=" ")"""
nomes.reverse()
print(nomes)