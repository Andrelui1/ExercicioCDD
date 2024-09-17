pin = 123
senha = int(input("Digite sua senha: "))
tentativa = 1
while senha != pin and tentativa < 3:
    senha = int(input(f"senha invalida, digite novamente\n"
                      f"voce tem: {3 - tentativa} "))

    tentativa += 1
if tentativa == 3 and senha != pin:
    print("Senha bloqueada ")
else:
    print("passou")