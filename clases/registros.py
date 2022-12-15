import sqlite3
import datetime
class RegAdmin:
    def __init__(self,id=0,id_audi=0,id_usr=0,fechayhora=datetime.now()):
        self._id=id
        self._audi=id_audi
        self._usr=id_usr
        self._fechayhora=fechayhora
        
