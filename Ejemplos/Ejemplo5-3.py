contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1
    print("interacción:", contador)
    if contador == 3:
        print("Se ha alcanzado el valor 3, saliendo del bucle.")
        break
print ("Fin del bucle.")