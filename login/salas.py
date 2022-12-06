class Sala:
    def __init__(self,id,capacidad,tipo):
        self._id=id
        self._capacidad=capacidad
        self._tipo=tipo

    @property
    def id (self):
        return self._id
    @id.setter
    def id (self,otro):
        self._id=otro
    @property
    def capacidad(self):
        return self._capacidad
    @capacidad.setter
    def capacidad (self,otro):
        self._capacidad= otro
    @property
    def tipo (self):
        return self._tipo
    @tipo.setter
    def tipo (self,otro):
        self._tipo=otro
    

sala1=Sala(1,45,"3D")
sala1.capacidad=23

print(sala1.capacidad)