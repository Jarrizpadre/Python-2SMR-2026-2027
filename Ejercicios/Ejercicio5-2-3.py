
var1 = int(input("Introduce el primer numero: "))
var2 = int(input("Introduce el segundo numero: "))

suma_pares = 0
suma_impares = 0

var2 += 1

for i in range(var1, var2):
    if i % 2 == 0:
        suma_pares += i
        print(f"Par: {i}")
    else:
        suma_impares += i
        print(f"Impar: {i}")

print(f"La suma de los pares es: {suma_pares}")
print(f"La suma de los impares es: {suma_impares}")

