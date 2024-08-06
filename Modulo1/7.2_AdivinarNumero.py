"""
Desarrolla un programa en el que el usuario ingrese un número entre 0 y 9.
 El programa debe solicitar al usuario que adivine el número correcto de manera iterativa, es decir, 
 seguirá preguntando hasta que el usuario adivine el número correctamente.
 """
Nsecreto = 3

adivinado = False
while (adivinado == False):
    num = int(input("Introduzca un número por favor: "))
    if (num == Nsecreto):
        print("Felicidades")
        adivinado = True
    else:
        print("Intentelo de nuevo")