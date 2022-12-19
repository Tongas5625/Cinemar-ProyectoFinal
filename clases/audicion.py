import sqlite3
#from datetime import datetime
#from pelicula import Pelicula
from datetime import date, time, datetime
#from butaca import Butaca
#from sala import Sala
class Audicion:
    def __init__(self,id=0,pelicula=0,sala=0,fecha=date.today(),hora=time(22, 39)):#
        self.base_de_datos()
        self._id=id
        self._pelicula=pelicula
        self._sala=sala
        self._fecha=fecha #recibe en formato 2019-12-04   
        self._hora=hora #time(hh,mm,ss)
        
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
    def fecha(self,fecha):
        self._fecha=fecha
               
        
    @property
    def hora(self):
        return self._hora
    
    @hora.setter
    def hora(self,hora):
        hoy=date.today()
        if(self._fecha>=hoy):           #puede ser hoy pero no ayer
            self._hora=hora
            return True        
        else:
            print("setear primero fecha")
            return False
    
    def base_de_datos(self):
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS audiciones (id	INTEGER, Pelicula	INTEGER,Sala INTEGER, Fecha TEXT,Hora TEXT,PRIMARY KEY(id AUTOINCREMENT));")
        conexion.commit()
        conexion.close()
   
    def grabar_datos(self): #inserta datos
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        print(f"INSERT INTO audiciones (Pelicula, Sala, Fecha, Hora) VALUES ({self._pelicula},{self._sala},'{self._fecha}','{self._hora}');")
        cursor.execute(f"INSERT INTO audiciones (Pelicula, Sala, Fecha, Hora) VALUES ({self._pelicula},{self._sala},'{self._fecha}','{self._hora}');")
        print("grabando datos de audiciones en base de audiciones")
        conexion.commit()
        conexion.close()
    
    def get_id_db(self):
        self.grabar_datos()
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT id FROM audiciones WHERE Pelicula={self._pelicula} AND Fecha='{self._fecha}' AND Hora='{self._hora}' AND Sala={self._sala};")
        mem=cursor.fetchone()
        self._id=mem[0]
        conexion.close()
        print (mem[0]) 
        
    def modificar(self):
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        print(f"UPDATE audiciones SET Pelicula={self._pelicula}, Fecha='{self._fecha}', Hora='{self._hora}', Sala={self._sala} WHERE id={self._id};")
        cursor.execute(f"UPDATE audiciones SET Pelicula={self._pelicula}, Fecha='{self._fecha}', Hora='{self._hora}', Sala={self._sala} WHERE id={self._id};")
        conexion.commit()
        conexion.close
        
    def eliminar(self):
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        cursor.execute(f"DELETE FROM audiciones WHERE id={self._id};")
        conexion.commit()
        conexion.close
        
    def recup_audi_pelisid(self,pelis_id):#devuelve lista de id de audiciones con la misma pelicula
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT id FROM audiciones WHERE Pelicula={pelis_id};")
        audilist=cursor.fetchall()
        conexion.close
        if audilist:
            return audilist
        else:
            print("no hay audiciones con esa pelicula")
            
    def recup_audi_id(self,id):#rellena con datos de db
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT * FROM audiciones WHERE id={id};")
        audi=cursor.fetchall()
        conexion.close
        print(f"contenido de audi {audi}")
        if audi:
            self._id=audi[0][0]
            self._pelicula=audi[0][1]
            self._sala=audi[0][2]
            self._fecha=audi[0][3]
            self._hora=audi[0][4]    
        else:
            print("id de audicion no encontrado")
    
    def horarios_audiypeli(self,id_peli,fecha):#devuelve una lista de horarios para audi y peli
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        print(f"SELECT Hora FROM audiciones WHERE Pelicula={id_peli} AND Fecha='{fecha}';")
        cursor.execute(f"SELECT Hora FROM audiciones WHERE Pelicula={id_peli} AND Fecha='{fecha}';")
        horarioslist=cursor.fetchall()
        conexion.close()
        if horarioslist:
            return horarioslist
        else:
            print("no hay horarios")
            
    def pelihorayfecha(self,id_peli,hora,fecha):
        conexion=sqlite3.connect("audiciones.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT id FROM audiciones WHERE Pelicula={id_peli} AND Fecha='{fecha}' AND Hora='{hora}';")
        audi=cursor.fetchone()
        conexion.close
        print(f"contenido de audi {audi}")
        if audi:
            self._id=audi[0]
            return self._id    
        else:
            print("id de audicion no encontrado")
        
            