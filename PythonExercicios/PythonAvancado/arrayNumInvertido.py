num = [""]*5
tamanho = len(num)
for i in range(tamanho):
    num[i] = int(input("Digite um numero: "))
for x in range(4,-1,-1):
    print(num[x], end=" ")
