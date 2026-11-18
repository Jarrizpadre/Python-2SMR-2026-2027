
var1 = int(input("introduce el primer numero: "))
var2 = int(input("Introduce el segundo numero: "))

suma = 0 
var2 += 1

for i in range(var1,var2):
    suma += i
    print(f"valor: {i}")
else:
    print(f"el sumatorio  es: {suma}")
