import sqlite3
class Pelicula:
    categorias = ("Accion", "Comedia", "Drama", "Suspenso") 
    def __init__(self, nombre="", director="", duracion="", fechaEstreno="", clasificacion=("primera","segunda","tercera"),categoria="Sin Asignar"):
        self.base_de_datos()
        self._nombre = nombre
        self._director = director
        self._categoria = categoria
        self._duracion = duracion
        self._fechaEstreno = fechaEstreno
        self._clasificacion = clasificacion
        self._id=0
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
    def nombre(self,nombre):
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
    def director(self,director):
        self._director = director
        
    @property
    def clasificacion(self):
        return self._clasificacion
    
    @clasificacion.setter
    def clasificacion(self,clasificacion):
        self._clasificacion = clasificacion
        
    def base_de_datos(self):
        conexion=sqlite3.connect("movies.db")
        cursor=conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pelis (id	INTEGER, Nombre	TEXT, Director	TEXT, Duracion	INTEGER, Estreno	TEXT, Clasificacion	TEXT, PRIMARY KEY(id AUTOINCREMENT))")
        conexion.commit()
        conexion.close()
            
    def grabar_datos(self):
        conexion=sqlite3.connect("movies.db")
        cursor=conexion.cursor()
        print(f"INSERT INTO pelis (Nombre, Director, Duracion, Estreno, Clasificacion) VALUES ('{self._nombre}','{self._director}','{self._duracion}','{self._fechaEstreno}','{self._clasificacion}');")
        cursor.execute(f"INSERT INTO pelis (Nombre, Director, Duracion, Estreno, Clasificacion) VALUES ('{self._nombre}','{self._director}','{self._duracion}','{self._fechaEstreno}','{self._clasificacion}');")
        print("grabando datos de pelis en base de datos")
        conexion.commit()
        conexion.close()
    
    def get_id_db(self):
        self.grabar_datos()
        conexion=sqlite3.connect("movies.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT id FROM pelis WHERE Nombre='{self._nombre}' AND Director='{self._director}' AND Duracion={self._duracion} AND Estreno='{self._fechaEstreno}';")
        mem=cursor.fetchone()
        self._id=mem[0]
        conexion.close()
        print (mem[0])       

    def rellena(self, lista): #se usa para rellenar cuando recupera
        self._id=lista[0][0]
        self._nombre=lista[0][1]
        self._director=lista[0][2]
        self._duracion=lista[0][3]
        self._fechaEstreno=lista[0][4]
        self._clasificacion=lista[0][5] 
        
        
        
    def recup_peli_db_id(self, id):
        conexion=sqlite3.connect("movies.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT * FROM pelis WHERE id={id};")
        mem=cursor.fetchall()
        print(mem[0][0])
        print(mem[0][4])
        conexion.close()
        self.rellena(mem)
        
    def recup_peli_db_nombre(self, nombre):
        conexion=sqlite3.connect("movies.db")
        cursor=conexion.cursor()
        cursor.execute(f"SELECT * FROM pelis WHERE Nombre='{nombre}';")
        mem=cursor.fetchall()
        if mem:
            print("ok")
        print(mem[0][3])
        print(mem)
        conexion.close()
        self.rellena(mem)
        print(self._id)
        
#mem=Pelicula()
#mem.recup_peli_db_nombre("The Volunteer")
#print(mem.duracion)


                             