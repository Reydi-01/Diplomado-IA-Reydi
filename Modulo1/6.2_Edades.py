edad = int(input("Introduzca su edad por favor: "))
if (edad < 13):
    print("Usted es un niño")
elif (edad < 18):
    print("Usted es un adolescente")
elif (edad < 65):
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")