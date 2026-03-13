from funciones import *

def main():

    animales = cargar_csv("zoo.csv")
    clases = cargar_csv("clases.csv")

    while True:

        opcion = mostrar_menu()

        if opcion == "1":
            listar_por_clase(animales, clases)

        elif opcion == "2":
            listar_por_caracteristica(animales)

        elif opcion == "3":
            agregar_animal(animales)

        elif opcion == "4":

            campos = animales[0].keys()
            guardar_csv("zoo.csv", animales, campos)

            print("Cambios guardados. Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()