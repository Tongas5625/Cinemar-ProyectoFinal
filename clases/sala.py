class Butacas:
    def _init_(self,id=0,numero=0,sala=0):
        self._id=id
        self._numero=numero
        self._sala=sala
        self._libre=True
        
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
    def sala(self):
        return self._sala
    
    @sala.setter
    def sala(self,sala):
        self._numero=sala 
        
    @property
    def libre(self):
        return self._libre
    
    @libre.setter
    def libre(self,libre):
        self._libre=libre
    
     

class Sala:
    def _init_(self,id=0,numero=0):
       self._id=id
       self._numero=numero
    
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
        
        
        
