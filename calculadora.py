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
    print("Bienvenido a la calculadora.")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        eleccion = input("Ingrese el número de la operación que desea realizar (1/2/3/4): ")

        if eleccion in ('1', '2', '3', '4'):
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if eleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")

            elif eleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")

            elif eleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            elif eleccion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

            siguiente = input("¿Quieres realizar otra operación? (sí/no): ")
            if siguiente.lower() != 'sí':
                break
        else:
            print("Operación no válida. Por favor, elige una opción válida.")

    print("Gracias por usar la calculadora. ¡Hasta luego!")

if __name__ == "__main__":
    main()
