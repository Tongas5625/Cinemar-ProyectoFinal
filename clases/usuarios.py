import sqlite3

class Usuario:
    def __init__(self,id=0, nombre='', apellido='', edad=0, dni=0, mail="", passw="123"):
        self.base_de_datos()
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni
        self.__mail = mail
        self.__passw = passw
        self.__esadmin = False
        self.__id=id

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id=id
       
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
    
    @mail.setter
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
        return self.__edad >= 18
    
    def esadmin(self):
        return self.__esadmin
    
    def haceradmin(self):
        self.__esadmin=True
        
    def base_de_datos(self):
        conexion=sqlite3.connect("user.db")
        cursor=conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id	INTEGER,Nombre	TEXT,Apellido	TEXT,Dni	INTEGER,Mail	TEXT,Passwd	TEXT,EsAdmin	INTEGER,PRIMARY KEY(id AUTOINCREMENT))")
        conexion.commit()
        conexion.close()
        
    def grabar_datos(self):
        conexion=sqlite3.connect("user.db")
        cursor=conexion.cursor()
        cursor.execute(f"INSERT INTO usuarios (Nombre, Apellido, Dni, Mail, Passwd) VALUES ('{self.__nombre}','{self.__apellido}',{self.__dni},'{self.__mail}','{self.__passw}')")
        conexion.commit()
        conexion.close()
    
    def get_id_db(self):
        self.grabar_datos()
        conexion=sqlite3.connect("user.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT id FROM usuarios WHERE Nombre='{self.__nombre}' AND Apellido='{self.__apellido}' AND Dni={self.__dni} AND Mail='{self.__mail}';")
        mem=cursor.fetchone()
        self.__id=mem[0]
        conexion.commit()
        conexion.close()
        print (mem[0])       
       
temp=Usuario(0,"fede","cruz",40,123123,"correo",12345)
temp.get_id_db()
print(temp.id)
