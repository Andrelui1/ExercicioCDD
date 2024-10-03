nomes = [""]*2
senhas = [""]*2
tamanho1 = len(nomes)
for x in range(tamanho1):
    nomes[x] = input("Digite um nome: ")
    senhas[x] = input("Digite uma senha: ")

for i in range(tamanho1):
    print(f"Nome: {nomes[i]}! Senha: {senhas[i]} e sua posiçao é {i}")

