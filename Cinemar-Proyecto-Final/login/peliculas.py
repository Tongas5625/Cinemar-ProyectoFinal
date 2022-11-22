class pelicula:
    
    def __init__(self, id, name, subtitles, description, duration, type):
        self.__id=id
        self.__name=name
        self.__subtitles=subtitles
        self.__description=description
        self.__duration=duration
        self.__type=type
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id=id
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name=name
        
    @property
    def subtitles(self):
        return self.__subtitles
    @subtitles.setter
    def subtitles(self, subtitles):
        self.__subtitles=subtitles
        
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description=description
    
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration=duration
        
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type=type
        
    def __str__(self):
        cadena= "\nID: "+str(self.__id)
        cadena+= "\nName: "+self.__name
        cadena+= "\nSubtitle: "+self.__subtitles
        cadena+= "\Description: "+self.__description
        cadena+= "\nDuration: "+str(self.__duration)
        cadena+= "\nType: "+self.__type
        return cadena    
    
peliculas = pelicula(1, 'Godzila VS KingKong ', 'Español', 'In this movie, these beasts will fight for conquer Manhatan, citi of New York!!', 120, '3D')
print(peliculas)
