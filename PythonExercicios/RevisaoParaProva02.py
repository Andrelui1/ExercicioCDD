opcao = 1
while opcao == 1:
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
       if num > 0:
           print("Numero Par positivo ")
       else:
           print("Numero Par negativo")
    else:
        if num > 0:
            print("Numero Impar positivo ")
        else:
            print("Numero Impar negativo")
    opcao = int(input("Voce quer fazer outra verificação:\n"
                      "1 para sim\n"
                      "2 para nao\n"))