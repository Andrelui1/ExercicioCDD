def par(n):
    if n % 2 == 0:
        print("Numero é par: ")
def impar(n):
    if n % 2 != 0:
        print("numero impar: ")

def imprimirNome(nome):
    print(f"Ola {nome}")

def piramide(num):
    for i in range(1, num + 1):
        for x in range(i):
            print(i, end=" ")
        print()
def piramide2(num):
    for i in range(1,num+1):
        for x in range(1, i+1):
            print(x, end=" ")
        print()

def vogais(texto1):
    cont = 0
    tamanho = len(texto1)
    for x in range(tamanho):
        if texto1[x] in "aeiou":
            cont +=1
    print(f"Encontramos {cont} vogais")

def letras (texto):
    tamanho = len(texto)
    cont = 0
    for x in texto:
        if x not in " ":
            cont += 1
    print(cont)
    print(texto[::-1])


def listaUnica(lista):
    novaLista = []
    for x in lista:
            if x not in novaLista:
             novaLista.append(x)
            print(novaLista)

a = [1,2,2,3,4,3,4,5,6,7,6,8,7,10]
listaUnica(a)

def primo(n):
    if(n==1):
        return n, 'não e primo'
    elif (n==2):
        return n,"é primo"
    else:
        for x in range(2,n):
            if(n % x ==0):
                return n, "Não é Primo"

        return n, "É primo"

