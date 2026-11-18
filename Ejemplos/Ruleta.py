

import random

saldo = 100

print("🎰 RULETA DE CASINO 🎰")
print("Tienes 100 fichas ficticias.")
print("Rojo: 1 | Negro: 2 | Verde (0): 3")

while saldo > 0:
    print(f"\nTu saldo: {saldo} fichas")

    apuesta = int(input("Cuantas fichas quieres apostar? (0 para salir): "))

    if apuesta == 0:
        break

    if apuesta < 0 or apuesta > saldo:
        print("Apuesta no valida.")
        continue

    print("\n1. Rojo")
    print("2. Negro")
    print("3. Verde (0)")
    opcion = int(input("Elige tu apuesta: "))

    if opcion not in [1, 2, 3]:
        print("Opcion no valida.")
        continue

    numero = random.randint(0, 36)

    if numero == 0:
        color = "Verde"
    elif numero in [1, 3, 5, 7, 9, 12, 14, 16, 18,
                    19, 21, 23, 25, 27, 30, 32, 34, 36]:
        color = "Rojo"
    else:
        color = "Negro"

    print("\nGirando la ruleta...")
    print(f"Ha salido el {numero} {color}")

    if (opcion == 1 and color == "Rojo") or \
       (opcion == 2 and color == "Negro") or \
       (opcion == 3 and color == "Verde"):
        if opcion == 3:
            ganancia = apuesta * 35
        else:
            ganancia = apuesta

        saldo += ganancia
        print(f"¡Has ganado {ganancia} fichas!")
    else:
        saldo -= apuesta
        print("Has perdido la apuesta.")

print(f"\nFin de la partida. Saldo final: {saldo} fichas.")
print("Gracias por jugar.")
