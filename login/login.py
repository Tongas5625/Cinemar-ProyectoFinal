class user:

    def __init__(self, id, name, surname, email, dni):

        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__dni = dni

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    def __str__(self):
        cadena = "\nID: "+str(self.__id)
        cadena += "\nName: "+self.__name
        cadena += "\nSurname: "+self.__surname
        cadena += "\nEmail: "+self.__email
        cadena += "\nD.N.I: "+str(self.__dni)
        return cadena


gaston = user(1, 'Gaston Alberto ', 'Padilla', 'gaston@gmail.com', 44697941)
paula = user(3, 'Paula Agostina ', 'Miranda', 'paula@hotmail.com', 43697423)
camila = user(2, 'Camila Zoe ', 'Altamirano', 'camila@gmail.com', 29635895)

print(gaston.name, paula.surname, camila.email)
