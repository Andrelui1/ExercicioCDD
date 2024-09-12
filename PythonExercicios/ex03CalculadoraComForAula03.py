
print(" === Digite um numero de 1 a 10 para calcular a tabuada do número escolhido === ")

numero = int(input("Digite um número: "))

for x in range (1, 11):
    resultado = numero * x

    print(f"{x} x {numero} = {resultado}")