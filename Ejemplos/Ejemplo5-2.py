
import random

num_adivinar = random.randint(1, 10)
intentos = 3

val = int(input("Adivina un número entre 1 y 10: "))

if val == num_adivinar:
    print("¡Felicidades! Adivinaste el número.")
else:
    print