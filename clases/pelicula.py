class Pelicula:
    categorias = ("Accion", "Comedia", "Drama", "Suspenso") 
    def _init_(self, nombre, director, duracion, fechaEstreno, clasificacion,categoria="Sin Asignar"):
        self._nombre = nombre
        self._director = director
        self._categoria = categoria
        self._duracion = duracion
        self._fechaEstreno = fechaEstreno
        self._clasificacion = clasificacion
        
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def id(self,nombre):
        self._nombre = nombre
    
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self,duracion):
        self._duracion = duracion

    @property
    def fechaEstreno(self):
        return self._fechaEstreno

    @fechaEstreno.setter
    def fechaEstreno(self,fechaEstreno):
        self._fechaEstreno = fechaEstreno

    @property
    def director(self):
        return self._director

    @director.setter
    def duracion(self,director):
        self._director = director
        
    @property
    def clasificacion(self):
        return self._clasificacion
    
    @clasificacion.setter
    def clasificacion(self,clasificacion):
        self._clasificacion = clasificacion
            
        