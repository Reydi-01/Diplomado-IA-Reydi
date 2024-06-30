Nsecreto = 3

adivinado = False
while (adivinado == False):
    num = int(input("Introduzca un número por favor: "))
    if (num == Nsecreto):
        print("Felicidades")
        adivinado = True
    else:
        print("Intentelo de nuevo")