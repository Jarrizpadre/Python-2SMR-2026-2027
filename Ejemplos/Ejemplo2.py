
import random
import time


def mostrar(Victor, Mistel):
    print("\033[H\033[J", end="")


    print("CARRERA DE AUTOBUSES")
    print("=" * 70)
    print()


    print(" " * Victor + "________________")
    print(" " * Victor + "|__|__|__|__|__|")
    print(" " * Victor + "|     Victor     |")
    print(" " * Victor + "|~o~~~~~~~~~o~|")


    print()


    print(" " * Mistel + "________________")
    print(" " * Mistel + "|__|__|__|__|__|")
    print(" " * Mistel + "|    Mistel      |")
    print(" " * Mistel + "|~o~~~~~~~~~o~|")


    print()
    print("=" * 70)




Victor = 0
Mistel = 0
meta = 50


input("Pulsa ENTER para comenzar la carrera...")


while Victor < meta and Mistel < meta:


    Victor += random.randint(1, 3)
    Mistel += random.randint(1, 3)


    if Victor > meta:
        Victor = meta


    if Mistel > meta:
        Mistel = meta


    mostrar(Victor, Mistel)


    time.sleep(0.2)


print()


if Victor == Mistel:
    print("EMPATE")
elif Victor > Mistel:
    print("¡VICTOR HA GANADO!")
else:
    print("¡MISTEL HA GANADO!")
