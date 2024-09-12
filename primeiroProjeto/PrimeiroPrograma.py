nome = input(("Qual é seu nome: "))
idade = int(input("Qual é a sua idade: "))
print(f"A seu nome é {nome} e sua idade é {idade}")
if idade >= 18:
    print("Voce é de maior. ")
else:
    print("Voce é de menor e não pode continuar, fim do programa.")