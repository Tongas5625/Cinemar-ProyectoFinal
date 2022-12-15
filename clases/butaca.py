import sqlite3


class Butaca:
    def __init__(self, id=0, numero=0, sala_id=0):
        self.base_de_datos()
        self._id = id
        self._numero = numero
        self._sala = sala_id
        self._libre = True

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def id(self, numero):
        self._numero = numero

    @property
    def sala(self):
        return self._sala

    @sala.setter
    def sala(self, sala):
        self._numero = sala

    @property
    def libre(self):
        return self._libre

    @libre.setter
    def libre(self, libre):
        self._libre = libre

    def base_de_datos(self):
        conexion = sqlite3.connect("butacas.db")
        cursor = conexion.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS butacas (id INTEGER, Sala INTEGER,Numero INTEGER, Libre	TEXT, PRIMARY KEY(id AUTOINCREMENT));")
        conexion.commit()
        conexion.close()

    def grabar_datos(self):  # inserta datos
        conexion = sqlite3.connect("butacas.db")
        cursor = conexion.cursor()
        print(
            f"INSERT INTO butacas (Sala, Numero, Libre) VALUES ('{self._sala}','{self._numero}','{self._libre}');")
        cursor.execute(
            f"INSERT INTO butacas (Sala, Numero, Libre) VALUES ('{self._sala}','{self._numero}','{self._libre}');")
        print("grabando datos de butacas en base de butacas db")
        conexion.commit()
        conexion.close()

    def get_id_db(self):
        self.grabar_datos()
        conexion = sqlite3.connect("butacas.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT id FROM butacas WHERE Numero='{self._numero}' AND Sala='{self._sala}' AND Libre={self._libre};")
        mem = cursor.fetchone()
        self._id = mem[0]
        conexion.close()
        print(mem[0])

    def modificar(self):
        conexion = sqlite3.connect("butacas.db")
        cursor = conexion.cursor()
        print(
            f"UPDATE butacas SET Numero={self._numero}, Sala='{self._sala}', Libre={self._libre}, WHERE id={self._id};")
        cursor.execute(
            f"UPDATE butacas SET Numero={self._numero}, Sala='{self._sala}', Libre={self._libre}, WHERE id={self._id};")
        conexion.close()

    def eliminar(self):
        conexion = sqlite3.connect("butacas.db")
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM butacas WHERE id={self._id};")
        conexion.commit()
        conexion.close()

    def rellena(self, lista):
        self._id = lista[0][0]
        self._numero = lista[0][1]
        self._sala = lista[0][2]
        self._libre = lista[0][3]

    def recup_usr_db_id(self, id):
        conexion = sqlite3.connect("butacas.db")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM reservas WHERE id={id};")
        mem = cursor.fetchall()
        print(mem[0][0])
        print(mem[0][4])
        conexion.close()
        self.rellena(mem)
