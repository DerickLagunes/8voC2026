class registro:
    def __init__(self, nombre_completo, matricula, correo, telefono, rfc, contrasena):
        self.nombre_completo = nombre_completo
        self.matricula = matricula
        self.correo = correo
        self.telefono = telefono
        self.rfc = rfc
        self.contrasena = contrasena

    def getNombre(self):
        return self.nombre_completo
    
    def saludar(self):
        return "Hola, {}. ¿Cómo estás?".format(self.nombre_completo)