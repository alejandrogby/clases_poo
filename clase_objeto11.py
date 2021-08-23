#clase y estatico

class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f"pastel({self.ingredientes !r})"
    
    @classmethod
    def Pastel_Chocolate(cls):
        return cls(["Harina", "Leche", "Chocolate"])

    @classmethod
    def Pastel_Vainilla(cls):
        return cls (["Harina", "Leche", "Vainilla"])

print(Pastel.Pastel_Chocolate())

