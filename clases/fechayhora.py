#para manejar fecha y hora con datetime
import datetime
from datetime import time
from datetime import date
class FechaHora:
    def __init__(dia=0,mes=0,year=0,hora=0,min=0):
        pass        
prueba=datetime.datetime.now()
print (prueba)
hoy=date.today()
yo=date(2023,9,19)

if (hoy>yo):
    print(hoy)
else:
    print(yo)
    
print (datetime.date.today())
print (datetime.time())
a=time()
b=a