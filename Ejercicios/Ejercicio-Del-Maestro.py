# Crear una Calculadora que realice las operaciones básicas de suma, resta, multiplicación y división.
X = int(input("Ingrese un número: "))
simbolo = input("Ingrese el símbolo de la operación (+, -, *, /): ")
Y = int(input("Ingrese otro número: "))

# Funcion eval(): Toma un texto y lo evalúa como una expresión de Python. En este caso, se utiliza para realizar la operación matemática ingresada por el usuario.
resultado = eval(f"{X} {simbolo} {Y}")

print (f"Resultado: {resultado}")


