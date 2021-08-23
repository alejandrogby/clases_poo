#Polimorfismo

class Animales:
    def __init__(self, nombre) :
        self.nombre = nombre
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print("Animal salvaje")

class Perro(Animales):
    def tipo_animal(self):
        print ("Animal Domestico")

nuevo_animal = Leon("Simba")
nuevo_animal.tipo_animal()

nuevo_animal2= Perro("Rex")
nuevo_animal2.tipo_animal()