soma = 0
for c in range(1, 5+1):
    numero = int(input(f"Digite o {c} valor: "))
    soma = soma + numero
print(soma)

contador = 1
while contador < 5+1:
    numero = int(input(f"Digite o {contador} valor: "))
    soma = soma + numero
    contador += 1
print(soma)