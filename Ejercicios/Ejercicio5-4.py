usuarios = "root"
password = "toor"

intentos = 3
while(intentos > 0):
    usuario = input("introduce nombre del usuario:")
    password = input("introduce la contraseña:")
    intentos = intentos -1

    if usuario == usuarios and password == password:
        print(f"¡Bienvenido!")
        break

    else:
        print (f"Te has equivocado picha")
        print(f"Te quedan {intentos} Intentos")
    
else:
    print("Por mis huevos que ya no accedes")



