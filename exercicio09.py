time1 = input("Qual é o nomme do time 1: ")
time2 = input("Qual é o nomme do time 2: ")
golsTime1 = int(input("Digite o numeros de gol(s) feito pelo time 1: "))
golsTime2 = int(input("Digite o numeros de gol(s) feito pelo time 2: "))
if golsTime1 > golsTime2:
    print(f"o time {time1}  venceu")
else:
   if golsTime1 == golsTime2:
       print("empate")
   else:
       print(f"o time {time2}  venceu")