opcao1 = 1
while opcao1 == 1:
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    opcao = int(input(
        "Digite 1 para soma\n"
        "Digite 2 para subtrair\n"
        "Digite 3 para multiplicar\n"
        "Digite 4 para dividir\n"
        "Digite 5 para digitar um novo numero\n"
        "Digite 6 para sair\n"))

    if opcao == 1:
        print(f"A soma entre o numero {num1} e {num2} é: {soma}")
    if opcao == 2:
        print(f"A subtração entre o numero {num1} - {num2} é: {sub}")
    if opcao == 3:
        print(f"A multiplicacao entre o numero {num1} e {num2} é: {mult}")
    if opcao == 4:
        print(f"A divisao entre o numero {num1} e {num2} é: {div}")
    if opcao == 5:
        print("Digite outro numero: ")
        opcao1 = 1
    if opcao == 6:
        opcao1 += 1
        break

    opcao1 = int(input("Deseja realizar outra operaca?\n"
                       "1 para sim\n"
                       "2 para sair\n"))
print("Fim do codigo")