
soma = 0

for x in range(1, 11, 1):
    numero = int(input(f"Digite {x}° numero inteiro: "))
    if numero % 2 !=0:
        soma = soma + numero
print(soma)