class alumno:
    def __init__(self, nombre, apellido, edad, matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula

    def getNombre(self):
        return self.nombre
    
    def saludar(self):
        return "Hola, {}. ¿Cómo estás?".format(self.nombre)