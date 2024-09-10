hora1 = int(input("Digete a hora: "))
minuto1 = int(input("Digite os minutos: "))

hora2 = int(input("Digete a hora: "))
minuto2 = int(input("Digite os minutos: "))

if hora1 > 12 or hora1 < 0:
    print("Erro")

elif minuto1 > 59 or minuto1 < 0:
    print("Erro")

elif hora2 > 24 or hora1 < 0:
    print("erro")

elif minuto2 > 59 or minuto2< 0:
    print("Erro")

somaHora = hora1 + hora2
somaM2 = minuto1 + minuto2
