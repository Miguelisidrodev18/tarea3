def ordenar_ascendentemente(num1, num2, num3):

    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros


def main():

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        numeros_ordenados = ordenar_ascendentemente(num1, num2, num3)
        print("Los números ordenados ascendentemente son:", numeros_ordenados)
    except ValueError:
        print("Error: Ingrese números válidos.")


if __name__ == "__main__":
    main()