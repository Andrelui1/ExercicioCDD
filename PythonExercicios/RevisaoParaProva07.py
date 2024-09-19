peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura**2
print(f"SEU PESO É: {peso:.2f}\ne por isso voce esta: ")
if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.6 and imc < 24.9:
    print("Peso ideal! Parabens.")
elif imc >= 25.0 and imc < 30:
    print("Levemente acima do peso")
elif imc >= 30.0 and imc < 35:
    print("Obesidade grau 1")
elif imc >= 35.0 and imc < 40:
    print("Obesidade grau 2 (severa) ")
elif imc >= 40:
    print("Obesidade grau 3 (morbida)")

