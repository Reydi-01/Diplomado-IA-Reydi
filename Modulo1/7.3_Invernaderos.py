"""Se le pide al usuario que ingrese los datos de temperatura y humedad para diferentes invernaderos.
 El programa analizará estos datos para determinar si se necesitan acciones como riego o ventilación. Las condiciones específicas son:
1.Si la temperatura es mayor a 30 grados, pero la humedad es mayor o igual al 30%, solo se recomienda ventilación.
2.Si la temperatura es mayor a 30 grados y la humedad es menor al 30%, se recomienda riego y ventilación.
3.Si la temperatura es menor o igual a 30 grados y la humedad es menor al 30%, solo se recomienda riego.
4.Si la temperatura es menor o igual a 30 grados y la humedad es mayor o igual al 30%, no se necesitan acciones."""
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
