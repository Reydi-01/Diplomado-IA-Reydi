""""
Realizar un programa que clasifique las edades de una persona, de la siguiente manera
1.Solicitar que el usuario ingrese su edad
2.El programa debe clasificar entre las siguientes categorías
a.Niño: Si la edad es menor a 13 años
b. Adolescente: Si la edad esta entre 13 y 17 años
c.Adulto: Si la edad es de 18 a 64 años
d. Adulto mayor: Si la edad es de 65 años o mas
"""

edad = int(input("Introduzca su edad por favor: "))
if (edad < 13):
    print("Usted es un niño")
elif (edad < 18):
    print("Usted es un adolescente")
elif (edad < 65):
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")