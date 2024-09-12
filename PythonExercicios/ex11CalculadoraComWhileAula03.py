opcao = 1
while opcao == 1:
    numero = int(input("Digite um valor: "))
    contador = 1


    while contador < 11:
        resultado = numero * contador
        print(f"{contador} x {numero} = {resultado}")
        contador += 1
    opcao = int(input("Deseja continuar: \n"
                      "1 para sim\n"
                      "2 para não\n"))
print("Fim do codigo")