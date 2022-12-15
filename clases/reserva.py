import sqlite3


class Reserva:
    # recibe butaca.id recibe id de usr
    def __init__(self, id=0, butaca=0, audicion=0, entradas=0, usuario=0):
        self.base_de_datos()
        self._id = id
        self._butaca = butaca
        self._audicion = audicion
        self._entradas = entradas
        self._usuario = usuario

    @property
    def id(self):
        return id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def butaca(self):
        return (self._butaca)

    @butaca.setter
    def butaca(self, butaca):
        self._butaca = butaca

    @property
    def audicion(self):
        return self.audicion

    @audicion.setter
    def audicion(self, audicion):
        self._audicion = audicion

    @property
    def entradas(self):
        return self._entradas

    @entradas.setter
    def entradas(self, entradas):
        self._entradas = entradas

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    def base_de_datos(self):
        conexion = sqlite3.connect("reservas.db")
        cursor = conexion.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS reservas (id	INTEGER, Butaca	INTEGER,Audicion INTEGER, Entrada INTEGER,Usuario TEXT,PRIMARY KEY(id AUTOINCREMENT));")
        conexion.commit()
        conexion.close()

    def grabar_datos(self):  # inserta datos
        conexion = sqlite3.connect("reservas.db")
        cursor = conexion.cursor()
        print(
            f"INSERT INTO reservas (Butaca, Audicion, Entrada, Usuario) VALUES ('{self._butaca}','{self._audicion}','{self._entradas}',{self._usuario});")
        cursor.execute(
            f"INSERT INTO reservas (Butaca, Audicion, Entrada, Usuario) VALUES ({self._butaca},{self._audicion},{self._entradas},{self._usuario});")
        print("grabando datos de reservas en base de reserva")
        conexion.commit()
        conexion.close()

    def get_id_db(self):
        self.grabar_datos()
        conexion = sqlite3.connect("reservas.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT id FROM reservas WHERE Butaca={self._butaca} AND Audicion={self._audicion} AND Entrada={self._entradas} AND Usuario='{self._usuario}';")
        mem = cursor.fetchone()
        self._id = mem[0]
        conexion.close()
        print(mem[0])

    def modificar(self):
        conexion = sqlite3.connect("reservas.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"UPDATE reservas SET Butaca='{self._butaca}', Audicion='{self._audicion}', Entrada={self._entradas}, Usuario='{self._usuario}' WHERE id={self._id};")
        conexion.commit()
        conexion.close

    def eliminar(self):
        conexion = sqlite3.connect("reservas.db")
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM reservas WHERE id={self._id};")
        conexion.commit()
        conexion.close

    def rellena(self, lista):
        self._id = lista[0][0]
        self._butaca = lista[0][1]
        self._audicion = lista[0][2]
        self._entradas = lista[0][3]
        self._usuario = lista[0][4]

    def recup_usr_db_id(self, id):
        conexion = sqlite3.connect("reservas.db")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM reservas WHERE id={id};")
        mem = cursor.fetchall()
        print(mem[0][0])
        print(mem[0][4])
        conexion.close()
        self.rellena(mem)
