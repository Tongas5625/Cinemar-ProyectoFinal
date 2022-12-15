import sqlite3
import sys

class Usuario:
    def __init__(self, id=0, nombre='', apellido='', dni=0, mail="", passw="123"):
        self.base_de_datos()
        self.__nombre = nombre
        self.__apellido = apellido
    #   self.__edad = edad
        self.__dni = dni
        self.__mail = mail
        self.__passw = passw
        self.__esadmin = False
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

#    @property
#    def edad(self):
#        return self.__edad

#    @edad.setter
#    def edad(self,edad):
#        self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, mail):
        self.__mail = mail

    @property
    def passw(self):
        return self.__passw

    @passw.setter
    def passw(self, passw):
        self.__passw = passw

    def __str__(self):
        return f"Nombre: {self.__nombre} \nId:  {self.__id}  \nMail: {self.__mail} \nEsAdmin: {self.__esadmin} "

#    def mayorEdad(self):
#        return self.__edad >= 18

    def esadmin(self):
        if (self.__esadmin == "True"):
            return True
        elif (self.__esadmin == "False"):
            return False
        print("grave error en self.__esadmin")

    def haceradmin(self):
        self.__esadmin = True

    def base_de_datos(self):
        conexion = sqlite3.connect("user.db")
        cursor = conexion.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios (id	INTEGER,Nombre	TEXT,Apellido	TEXT,Dni	INTEGER,Mail	TEXT,Passwd	TEXT,EsAdmin	INTEGER,PRIMARY KEY(id AUTOINCREMENT))")
        conexion.commit()
        conexion.close()

    def grabar_datos(self):
        conexion = sqlite3.connect("user.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"INSERT INTO usuarios (Nombre, Apellido, Dni, Mail, Passwd, EsAdmin) VALUES ('{self.__nombre}','{self.__apellido}',{self.__dni},'{self.__mail}','{self.__passw}','{self.__esadmin}')")
        conexion.commit()
        conexion.close()

    def get_id_db(self):
        self.grabar_datos()
        conexion = sqlite3.connect("user.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT id FROM usuarios WHERE Nombre='{self.__nombre}' AND Apellido='{self.__apellido}' AND Dni={self.__dni} AND Mail='{self.__mail}';")
        mem = cursor.fetchone()
        self.__id = mem[0]
        conexion.close()
        print(mem[0])

    def rellena(self, lista):
        self.__id = lista[0][0]
        self.__nombre = lista[0][1]
        self.__apellido = lista[0][2]
        self.__dni = lista[0][3]
        self.__mail = lista[0][4]
        self.__passw = lista[0][5]
        self.__esadmin = lista[0][6]

    def recup_usr_db_id(self, id):
        conexion = sqlite3.connect("user.db")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE id={id};")
        mem = cursor.fetchall()
        print(mem[0][0])
        print(mem[0][4])
        conexion.close()
        self.rellena(mem)

    def recup_usr_db_mail(self, mail):
        conexion = sqlite3.connect("user.db")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE Mail='{mail}';")
        mem = cursor.fetchall()
        conexion.close()
        if mem:
            self.rellena(mem)
            return True
        else:
            return False


"""temp=Usuario()

if (temp.recup_usr_db_mail("correo2@mail")):
    print(temp)
    print (f"dentro de temp.esadmin {temp.esadmin()}")
else:
    print("error")"""
# print(temp)
# print(temp.recup_usr_db_mail("errerea"))
# print(temp)
# temp=Usuario(0,"fede2022","cruz123",12312300,"correo@mail","12345")
# temp.get_id_db()
# print(temp.mail)
