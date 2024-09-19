a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
soma = a + b

print(f"A soma entre {a} e {b} é: {soma}")

if soma < c:
    print(f"a soma é entre {a} + {b} é menor do que c? Se soma for menor que c então print c: {c}")
else:
    print(soma)
    