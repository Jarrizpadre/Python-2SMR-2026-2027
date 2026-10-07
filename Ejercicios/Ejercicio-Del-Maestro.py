# Crear una Calculadora que realice las operaciones básicas de suma, resta, multiplicación y división.
X = int(input("Ingrese un número: "))
simbolo = input("Ingrese el símbolo de la operación (+, -, *, /): ")
Y = int(input("Ingrese otro número: "))
print(f"{X} {simbolo} {Y} es: { {"+": X + Y, "-": X - Y, "*": X * Y, "/": X / Y}[simbolo]}")


