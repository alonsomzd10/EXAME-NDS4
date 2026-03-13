class Animal:

    def __init__(self, nombre, clase, caracteristicas):
        self.nombre = nombre
        self.clase = clase
        self.caracteristicas = caracteristicas

    def __str__(self):
        return f"{self.nombre} - Clase: {self.clase}"

    def __repr__(self):
        return f"Animal({self.nombre}, {self.clase}, {self.caracteristicas})"