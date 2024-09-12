numero = 1
soma = 0
while numero <= 10:
    valores = float(input(f"Digite o {numero} valor: "))
    soma = (soma + valores) / valores
    numero += 1
print(soma)