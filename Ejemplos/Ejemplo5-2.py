
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
op = input("Ingrese la operación a realizar:")
if op == "+":
    print("El resultado de la suma es: ", num1 + num2)

elif op == "-":
    print("El resultado de la resta es: ", num1 - num2)

elif op == "*":
    print("El resultado de la multiplicación es: ", num1 * num2)

elif op == "/":
    if num2 == 0:
        print("No se puede dividir entre cero")
    else:
        print("El resultado de la división es: ", num1 / num2)