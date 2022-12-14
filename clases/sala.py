import sqlite3 

class Sala:
    def __init__(self,id=0,numero=0,tipo="2D",asientos=0):
       self.base_de_datos()
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
        self._asientos=asientos
    
    def base_de_datos(self):
        conexion=sqlite3.connect("salas.db")
        cursor=conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS salas (id INTEGER, Numero	INTEGER,Tipo TEXT, Asientos	INTEGER, PRIMARY KEY(id AUTOINCREMENT));")
        conexion.commit()
        conexion.close()
   
    def grabar_datos(self): #inserta datos
        conexion=sqlite3.connect("salas.db")
        cursor=conexion.cursor()
        print(f"INSERT INTO salas (Numero, Tipo, Asientos) VALUES ('{self._numero}','{self._tipo}','{self._asientos}');")
        cursor.execute(f"INSERT INTO salas (Numero, Tipo, Asientos) VALUES ('{self._numero}','{self._tipo}','{self._asientos}');")
        print("grabando datos de salas en base de sala")
        conexion.commit()
        conexion.close()
    
    def get_id_db(self):
        self.grabar_datos()
        conexion=sqlite3.connect("salas.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT id FROM salas WHERE Numero='{self._numero}' AND Tipo='{self._tipo}' AND Asientos={self._asientos};")
        mem=cursor.fetchone()
        self._id=mem[0]
        conexion.close()
        print (mem[0]) 
        
    def modificar(self):
        conexion=sqlite3.connect("salas.db")
        cursor=conexion.cursor()
        print(f"UPDATE salas SET Numero={self._numero}, Tipo='{self._tipo}', Asientos={self._asientos}, WHERE id={self._id};")
        cursor.execute(f"UPDATE salas SET Numero={self._numero}, Tipo='{self._tipo}', Asientos={self._asientos} WHERE id={self._id};")
        conexion.close()
        
    def eliminar(self):
        conexion=sqlite3.connect("salas.db")
        cursor=conexion.cursor()
        cursor.execute(f"DELETE FROM salas WHERE id={self._id};")
        conexion.commit()
        conexion.close()
        
    def rellena(self, lista):
        self._id=lista[0][0]
        self._numero=lista[0][1]
        self._tipo=lista[0][2]
        self._asientos=lista[0][3]
               
    def recup_usr_db_id(self, id):
        conexion=sqlite3.connect("salas.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT * FROM salas WHERE id={id};")
        mem=cursor.fetchall()
        print(mem[0][0])
        print(mem[0][4])
        conexion.close()
        self.rellena(mem)
