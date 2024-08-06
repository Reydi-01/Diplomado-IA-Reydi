"""""
Realice un programa que identifique entre números pares e impares:
1. Solicitar que el usuario ingrese un número 
2. Una vez que haya ingresado un número entero, el programa debe determinar si el número es par o impar
3. Muestre el resultado, indicando si el programa detetminó si es número par o impar
"""
N = int(input("Introduzca un número por favor: "))
if (N % 2 == 0):
    print("El número es par")
else:
    print("El número es impar")