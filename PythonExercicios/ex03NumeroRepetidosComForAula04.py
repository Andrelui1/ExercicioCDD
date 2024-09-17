numero = int(input("Digite um numero: "))
for i in range(numero + 1):
    for x in range(i):
        print(x, end=" ")
    print()