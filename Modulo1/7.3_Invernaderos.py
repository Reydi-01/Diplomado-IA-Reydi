contador = 0

while (contador < 3):

    temp = float(input("Introduzca la temperatura por favor: "))
    humedad = float(input("Introduzca la humedad por favor: "))

    if (temp > 30):
        if (humedad >= 30):
            accion = "Se recomienda ventilación"
        else: 
            accion = "Se recomienda riego y ventilación"
    elif(humedad > 30):
        accion = "No se necesitan acciones"
    else: 
        accion = "Se recomienda riego"
    contador += 1
    print(accion)
