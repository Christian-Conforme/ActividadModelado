import sys

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero."
    return x / y

def main():
    if len(sys.argv) > 1:
        # Argumentos desde la línea de comandos
        operacion = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])

        if operacion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif operacion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif operacion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif operacion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Operación no válida.")
    else:
        print("No se proporcionaron suficientes argumentos. Uso:")
        print("python calculadora.py <operacion> <num1> <num2>")
        print("Operaciones: 1 = Sumar, 2 = Restar, 3 = Multiplicar, 4 = Dividir")

if __name__ == "__main__":
    main()
