#Herencia Multiple
class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("Llamando...")
    def ocupado(self):
        print("Ocupado...")
    
class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("Tomando Fotos...")

class Reproduccion:
    def __init__(self):
        pass
    def reproductordemusica(self):
        print("Reproduciendo Musica")
    def reproductordevideo(self):
        print("Reproduciendo Video")

class Smarthphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print("Telefono Apagado")

movil = Smarthphone()
print(movil.llamar())