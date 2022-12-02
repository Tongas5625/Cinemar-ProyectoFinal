class Usuario:
    def _init_(self, nombre='', apellido='', edad=0, dni=0, mail="", pass="123"):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni
        self.__mail = mail
        self.__passw = passw

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        self.__dni = dni 
    
    @property
    def mail(self):
        return self.__mail
    
    @nombre.mail
    def mail(self,mail):
        self.__mail = mail
        
    @property
    def passw(self):
        return self.__passw
    
    @passw.setter
    def passw(self,passw):
        self.__passw = passw    
      

    def _str_(self):
        return "Nombre: " + self._nombre +"\nApellido: " + self.apellido + "\nEdad: "+ str(self.edad) + "\nDNI: " + str(self._dni)

    def mayorEdad(self):
        return self._edad >= 18