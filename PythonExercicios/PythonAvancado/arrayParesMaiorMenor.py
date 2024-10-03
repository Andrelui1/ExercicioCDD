numeros = [0]*3
tamanho = len(numeros)
maior = 0
menor = 100000000000
for x in range(tamanho):
    numeros[x] = int(input("Digite um numero: "))
print(numeros)
for x in range(tamanho):
    if numeros[x] % 2 == 0:
        print(f"o numero: {numeros[x]} é par")
for x in range(tamanho):
    if numeros[x] > maior:
        maior = numeros[x]
print(maior)
for x in numeros:
    if x < menor:
        menor = x
print(menor)