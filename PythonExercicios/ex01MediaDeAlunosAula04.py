opcao = 1
while opcao == 1:
        nota1 = float(input(f"Digite uma nota entre 0 e 10: "))
        nota2 = float(input(f"Digite uma nota entre 0 e 10: "))
        media = (nota1 + nota2) / 2
        while nota1 > 10 or nota1 < 0:
            print("nota valida")
            nota1 = int(input("Digite uma nota entre 0 e 10: "))

        while nota2 > 10 or nota2 < 0:
            print("nota invalida")
            nota2 = int(input("Digite uma nota entre 0 e 10: "))

        print(media)

        opcao = int(input("Digite 1 para realizar nova media\n"
              "digite 2 para sair\n"))
print('fim de codigo')



