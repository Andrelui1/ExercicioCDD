opcao = 1
while opcao == 1:
    numero1 = int(input("Digite um valor: "))
    numero2 = int(input("Digite outro valor: "))
    opcao = 1
    while numero2 == 0:
        numero2 = int(input("Digite um valor diferente de 0: "))
    div = numero1 / numero2
    print(div)
    opcao = int(input("Deseja continuar: \n"
                      "1 para sim\n"
                      "2 para não\n"))



print("Fim de codigo")