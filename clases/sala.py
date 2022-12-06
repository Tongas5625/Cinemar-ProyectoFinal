  

class Sala:
    def _init_(self,id=0,numero=0,tipo="2D",asientos=0):
       self._id=id
       self._numero=numero
       self._tipo=tipo
       self._asientos=asientos
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        self._id=id
        
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def id(self,numero):
        self._numero=numero
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self,tipo):
        self._tipo=tipo
        
    @property
    def asientos(self):
        return self._asientos
    
    @asientos.setter
    def asientos(self,asientos):
        self.asientos=asientos
    
   
        
        
        
