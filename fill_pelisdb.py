import sqlite3
from clases.pelicula import Pelicula
#rellena movies db desde la base de datos de imdb 
conexion=sqlite3.connect("imdb.db")
cursor=conexion.cursor()
cursor.execute(f"SELECT * FROM basics WHERE startYear=2022 AND titleType='movie' AND genres!='Documentary' AND runtimeMinutes>48 AND genres!='Adult' AND genres!='\\N' AND runtimeMinutes!='\\N';")
pelis=cursor.fetchall()
cursor.execute(f"UPDATE name SET primaryName = REPLACE(primaryName,'''','´');")
for i in range(500):
    print(pelis[i][0])
    cursor.execute(f"SELECT nconst FROM principals WHERE tconst='{pelis[i][0]}' AND category='director';")
    nconst=cursor.fetchone()
    if (nconst!=None):
        print(f"{nconst[0]}")
        cursor.execute(f"SELECT primaryName FROM name WHERE nconst='{nconst[0]}';")
        director=cursor.fetchone()
        print(f"{pelis[i][2]},{director[0]},{pelis[i][7]},{pelis[i][5]},{pelis[i][8]},""")
        pelicula=Pelicula(pelis[i][2],str(director[0]),pelis[i][7],pelis[i][5],pelis[i][8],"")
        pelicula.grabar_datos()
    


