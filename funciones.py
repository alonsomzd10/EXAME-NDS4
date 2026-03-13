import csv
from animal import Animal

def cargar_csv(nombre_archivo):

    datos = []

    with open(nombre_archivo, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            datos.append(fila)

    return datos


# guardar CSV
def guardar_csv(nombre_archivo, datos, campos):

    with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for fila in datos:
            escritor.writerow(fila)


# menu
def mostrar_menu():

    print("\n===== ZOOLOGICO =====")
    print("1. Listar animales por clase")
    print("2. Listar animales por característica")
    print("3. Agregar nuevo animal")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    return opcion


# listar por clase
def listar_por_clase(animales, clases):

    print("\nClases disponibles:")

    for c in clases:
        print(c["Clase_id"], "-", c["Clase_tipo"])

    seleccion = input("Seleccione el número de clase: ")

    for animal in animales:
        if animal["clase"] == seleccion:
            print(animal["nombre_animal"])


# listar por caracteristica
def listar_por_caracteristica(animales):

    caracteristica = input("Ingrese característica (pelo, plumas, cola, domestico etc): ")

    for animal in animales:

        if caracteristica in animal:

            if animal[caracteristica] == "1":
                print(animal["nombre_animal"])


# agregar animal
def agregar_animal(animales):

    nombre = input("Nombre del animal: ")
    clase = input("Clase (numero): ")

    nuevo = {
        "nombre_animal": nombre,
        "pelo": input("Tiene pelo? (1/0): "),
        "plumas": input("Tiene plumas? (1/0): "),
        "huevos": input("Pone huevos? (1/0): "),
        "leche": input("Da leche? (1/0): "),
        "volador": input("Puede volar? (1/0): "),
        "acuatico": input("Es acuatico? (1/0): "),
        "depredador": input("Es depredador? (1/0): "),
        "dientes": input("Tiene dientes? (1/0): "),
        "espina": input("Tiene espina dorsal? (1/0): "),
        "respira": input("Respira aire? (1/0): "),
        "venenoso": input("Es venenoso? (1/0): "),
        "aletas": input("Tiene aletas? (1/0): "),
        "cola": input("Tiene cola? (1/0): "),
        "domestico": input("Es domestico? (1/0): "),
        "tamanio_gato": input("Tamaño gato? (1/0): "),
        "clase": clase
    }

    animales.append(nuevo)

    print("Animal agregado correctamente")