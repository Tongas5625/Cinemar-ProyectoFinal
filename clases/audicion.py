from datetime import datetime
from pelicula import Pelicula

class Audicion:
    def _init_(self,id=0,pelicula=0,sala=0,fecha=datetime(2022,1,1,12,00),hora=datetime(2022,1,1,12,00)):#atentos pelicula y sala esta clase recibira el entero id de cada unas peliculas.id sala.id
        self._id=id
        self._pelicula=pelicula
        self._sala=sala
        self._fecha=fecha
        self._hora=hora
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        self._id=id
    
    @property
    def pelicula(self):
        return self._pelicula
    
    @pelicula.setter
    def pelicula(self,pelicula):
        self._pelicula=pelicula
        
    @property
    def sala(self):
        return self._sala
    
    @sala.setter
    def sala(self,sala):
        self._sala=sala
        
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def id(self,fecha):
        self._fecha=fecha
        
    @property
    def hora(self):
        return self._hora
    
    @hora.setter
    def hora(self,hora):
        self._hora=hora
    