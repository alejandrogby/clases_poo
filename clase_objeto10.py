#f-strings

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self):
        return f"Hola soy {self.nombre} {self.apellido} tengo {self.edad} años"

nuevo_estudiante= Estudiante("Victor","Cruz", 17)
print(f"{nuevo_estudiante !r}")
