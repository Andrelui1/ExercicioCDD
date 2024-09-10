litrosCombustivel = float(input("Digite a quantidade de litros: "))
tipoCombustivel = (input("Digite o tipo de combustivel: "))
if tipoCombustivel == "g":
    print(litrosCombustivel * 5.80)
else:
    print(litrosCombustivel * 4.90)
