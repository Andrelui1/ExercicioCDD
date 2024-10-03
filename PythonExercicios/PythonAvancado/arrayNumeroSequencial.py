novoNumero = 0
numeros = [0]*2
tamanho = len(numeros)
for x in range(tamanho):
    numeros[x] = int(input("Digite um numero: "))
novoNumero = int(input("Digite outro numero: "))
print(numeros.count(novoNumero))


