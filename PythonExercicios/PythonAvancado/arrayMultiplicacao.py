A = [""]*5
M = [""]*5
tamanho = len(A)
for i in range(tamanho):
    A[i] = int(input("Digite numero: "))
mult = int(input("Digite outro numero: "))

for x in range(tamanho):
   M[x] = A[i] * mult
print(A)
print(mult)
print(M)