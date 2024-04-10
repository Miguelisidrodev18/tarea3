import math


# Función para convertir grados a radianes
def grados_a_radianes(grados):
    return (math.pi / 180) * grados


# Función para convertir radianes a grados
def radianes_a_grados(radianes):
    return (180 / math.pi) * radianes


# Función para validar la entrada del usuario
def validar_opcion(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and int(valor) in [0, 1, 2]:
            return int(valor)
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 0.")


# Función principal
def main():
    while True:
        # Menú de opciones
        print("\n¿Qué conversión deseas realizar?")
        print("1. De grados a radianes")
        print("2. De radianes a grados")
        print("0. Salir")

        # Solicitar opción al usuario
        opcion = validar_opcion("Selecciona una opción (1, 2 o 0 para salir): ")

        # Salir del programa si el usuario selecciona la opción 0
        if opcion == 0:
            print("¡Hasta luego!")
            break

        # Realizar la conversión según la opción seleccionada
        elif opcion == 1:
            grados = float(input("Introduce los grados: "))
            radianes = grados_a_radianes(grados)
            print(f"{grados} grados = {radianes} radianes")
        elif opcion == 2:
            radianes = float(input("Introduce los radianes: "))
            grados = radianes_a_grados(radianes)
            print(f"{radianes} radianes = {grados} grados")


if __name__ == "__main__":
    main()