


class Reserva:
    def _init_(self,id=0,butaca=0,audicion=0,entradas=0,usuario=0):#recibe butaca.id recibe id de usr
       self._id=id
       self._butaca=butaca
       self._audicion=audicion
       self._entradas=entradas
       self._usuario=usuario
    
    @property
    def id(self):
        return id
    
    @id.setter
    def id(self,id):
        self._id=id
        
    @property
    def butaca(self):
        return(self._butaca)
    
    @butaca.setter
    def butaca(self,butaca):
        self._butaca=butaca
        
    @property
    def audicion(self):
        return self.audicion
    
    @audicion.setter
    def audicion(self,audicion):
        self._audicion=audicion
        
    @property
    def entradas(self):
        return self._entradas
    
    @entradas.setter
    def entradas(self, entradas):
        self._entradas=entradas
        
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario):
        self._usuario=usuario
    
       
       
       