import random

num_adivinar = random.randint(1, 100)
intentos = 5

print ("bienvenido al juego")

while intentos > 0:
    val = int(input("Adivina un número entre 1 y 100: "))
    intentos -= 1
    
    if num_adivinar == val:
        print("¡Felicidades! Adivinaste el número.")
        break

    elif num_adivinar > val:
        print(f"El número introducido es mayor {val}")
        print(f"Incorrecto. Te quedan {intentos} intentos.")

    elif num_adivinar < val:
        print(f"El número introducido es menor {val}")
        print(f"Incorrecto. Te quedan {intentos} intentos.")
else:
    print(f"Lo siento, no adivinaste el número. El número correcto era {num_adivinar}.")