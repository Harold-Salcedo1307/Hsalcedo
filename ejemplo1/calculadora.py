def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def calculadora():
    print("--- CALCULADORA BÁSICA ---")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Introduce el número de la operación (1/2/3/4): ")

    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: Por favor, introduce solo números válidos.")
            return

        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

# Ejecutar la calculadora
calculadora()