#funciones para atributos

class Persona:
    edad = 27
    nombre = "Victor"
    pais = "Brasil"

doctor = Persona()
#print("El doctor tiene unad edad?",hasattr(doctor,"apellido"))

# print("antes era : ",doctor.nombre)
# setattr(doctor,"nombre","Paquito")
# print("ahora se llama : ", doctor.nombre)

delattr(Persona, "pais")
print(doctor.pais