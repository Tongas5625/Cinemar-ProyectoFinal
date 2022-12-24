import tkinter as tk
import tkinter.font as tkFont
from clases.pelicula import Pelicula
from clases.sala import Sala
from clases.audicion import Audicion
from clases.butaca import Butaca
from datetime import date, time
#from alerta import Alerta
from tkinter import messagebox
def validate(input):
      
    if input.isdigit():
        return input
    else:
        return False
                      
    

class AudiAdminMenu:
    def __init__(self, root, peli=Pelicula(), sala=Sala()):
        root.focus()
        root.grab_set()
        self.sala=sala
        self.peli=peli
        #setting title
        root.title("Audicion Confirma Fecha Y Hora")
        #setting window size
        reg = root.register(validate)
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_49=tk.Label(root)
        GLabel_49["bg"] = "#5fb878"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_49["font"] = ft
        GLabel_49["fg"] = "#333333"
        GLabel_49["justify"] = "center"
        GLabel_49["text"] = "ADMINISTRACION"
        GLabel_49.place(x=70,y=20,width=460,height=40)

        GLabel_306=tk.Label(root)
        GLabel_306["activebackground"] = "#1e9fff"
        GLabel_306["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_306["font"] = ft
        GLabel_306["fg"] = "#333333"
        GLabel_306["justify"] = "center"
        GLabel_306["text"] = "SALA"
        GLabel_306.place(x=10,y=80,width=220,height=40)

        GLabel_213=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_213["font"] = ft
        GLabel_213["fg"] = "#333333"
        GLabel_213["justify"] = "center"
        GLabel_213["text"] = "Numero"
        GLabel_213.place(x=0,y=140,width=70,height=25)

        GLabel_323=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_323["font"] = ft
        GLabel_323["fg"] = "#333333"
        GLabel_323["justify"] = "center"
        GLabel_323["text"] = "Tipo"
        GLabel_323.place(x=0,y=190,width=70,height=25)

        GLabel_874=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_874["font"] = ft
        GLabel_874["fg"] = "#333333"
        GLabel_874["justify"] = "center"
        GLabel_874["text"] = "Asientos"
        GLabel_874.place(x=0,y=250,width=70,height=25)

        NumSalaLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        NumSalaLab["font"] = ft
        NumSalaLab["fg"] = "#333333"
        NumSalaLab["justify"] = "center"
        NumSalaLab["text"] = str(sala.numero)
        NumSalaLab.place(x=100,y=140,width=70,height=25)
        TipoSalaLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        TipoSalaLab["font"] = ft
        TipoSalaLab["fg"] = "#333333"
        TipoSalaLab["justify"] = "center"
        TipoSalaLab["text"] = str(sala.tipo)
        TipoSalaLab.place(x=100,y=190,width=70,height=25)

        AsientosSalaLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        AsientosSalaLab["font"] = ft
        AsientosSalaLab["fg"] = "#333333"
        AsientosSalaLab["justify"] = "center"
        AsientosSalaLab["text"] = str(sala.asientos)
        AsientosSalaLab.place(x=100,y=250,width=70,height=25)

        GLabel_343=tk.Label(root)
        GLabel_343["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_343["font"] = ft
        GLabel_343["fg"] = "#333333"
        GLabel_343["justify"] = "center"
        GLabel_343["text"] = "PELICULA"
        GLabel_343.place(x=230,y=80,width=347,height=40)

        GLabel_546=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_546["font"] = ft
        GLabel_546["fg"] = "#333333"
        GLabel_546["justify"] = "center"
        GLabel_546["text"] = "Titulo"
        GLabel_546.place(x=250,y=140,width=70,height=25)

        GLabel_968=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_968["font"] = ft
        GLabel_968["fg"] = "#333333"
        GLabel_968["justify"] = "center"
        GLabel_968["text"] = "Director"
        GLabel_968.place(x=250,y=190,width=70,height=25)

        GLabel_789=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_789["font"] = ft
        GLabel_789["fg"] = "#333333"
        GLabel_789["justify"] = "center"
        GLabel_789["text"] = "Año"
        GLabel_789.place(x=250,y=250,width=70,height=25)

        GLabel_202=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_202["font"] = ft
        GLabel_202["fg"] = "#333333"
        GLabel_202["justify"] = "center"
        GLabel_202["text"] = "Genero"
        GLabel_202.place(x=250,y=300,width=70,height=25)

        NombPeliLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        NombPeliLab["font"] = ft
        NombPeliLab["fg"] = "#333333"
        NombPeliLab["justify"] = "center"
        NombPeliLab["text"] = peli.nombre
        NombPeliLab.place(x=340,y=140,width=214,height=30)

        DirectPeliLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        DirectPeliLab["font"] = ft
        DirectPeliLab["fg"] = "#333333"
        DirectPeliLab["justify"] = "center"
        DirectPeliLab["text"] = peli.director
        DirectPeliLab.place(x=350,y=190,width=193,height=30)

        FechaPeliLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        FechaPeliLab["font"] = ft
        FechaPeliLab["fg"] = "#333333"
        FechaPeliLab["justify"] = "center"
        FechaPeliLab["text"] = peli.fechaEstreno
        FechaPeliLab.place(x=350,y=250,width=188,height=30)

        GeneroPeliLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GeneroPeliLab["font"] = ft
        GeneroPeliLab["fg"] = "#333333"
        GeneroPeliLab["justify"] = "center"
        GeneroPeliLab["text"] = peli.clasificacion
        GeneroPeliLab.place(x=380,y=300,width=122,height=30)

        FechaAudiLab=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        FechaAudiLab["font"] = ft
        FechaAudiLab["fg"] = "#333333"
        FechaAudiLab["justify"] = "center"
        FechaAudiLab["text"] = "Fecha"
        FechaAudiLab.place(x=0,y=350,width=70,height=25)

        GLabel_467=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_467["font"] = ft
        GLabel_467["fg"] = "#333333"
        GLabel_467["justify"] = "center"
        GLabel_467["text"] = "Hora"
        GLabel_467.place(x=0,y=380,width=70,height=25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

        self.DiaAudiBox=tk.Entry(root)
        self.DiaAudiBox.config(validate="key", validatecommand=(validate, '%P'))
        self.DiaAudiBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.DiaAudiBox["font"] = ft
        self.DiaAudiBox["fg"] = "#333333"
        self.DiaAudiBox["justify"] = "center"
        self.DiaAudiBox["text"] = "dia"
        self.DiaAudiBox.place(x=60,y=340,width=30,height=25)
                
        self.MesAudiBox=tk.Entry(root)
        self.MesAudiBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.MesAudiBox["font"] = ft
        self.MesAudiBox["fg"] = "#333333"
        self.MesAudiBox["justify"] = "center"
        self.MesAudiBox["text"] = "mes"
        self.MesAudiBox.place(x=95,y=340,width=30,height=25)
        
        self.YearAudiBox=tk.Entry(root)
        self.YearAudiBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.YearAudiBox["font"] = ft
        self.YearAudiBox["fg"] = "#333333"
        self.YearAudiBox["justify"] = "center"
        self.YearAudiBox["text"] = "año"
        self.YearAudiBox.place(x=130,y=340,width=30,height=25)

        self.HoraAudiBox=tk.Entry(root)
        self.HoraAudiBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.HoraAudiBox["font"] = ft
        self.HoraAudiBox["fg"] = "#333333"
        self.HoraAudiBox["justify"] = "center"
        self.HoraAudiBox["text"] = "horabox"
        self.HoraAudiBox.place(x=60,y=375,width=30,height=25)

        self.MinAudiBox=tk.Entry(root)
        self.MinAudiBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.MinAudiBox["font"] = ft
        self.MinAudiBox["fg"] = "#333333"
        self.MinAudiBox["justify"] = "center"
        self.MinAudiBox["text"] = "minbox"
        self.MinAudiBox.place(x=100,y=375,width=30,height=25)

        GButton_701=tk.Button(root)
        GButton_701["bg"] = "#75FF46"
        ft = tkFont.Font(family='Comics',size=13)
        GButton_701["font"] = ft
        GButton_701["fg"] = "#000000"
        GButton_701["justify"] = "center"
        GButton_701["text"] = "Confirmar"
        GButton_701.place(x=230,y=360,width=91,height=30)
        GButton_701["command"] = self.GButton_701_command
        
        AtrasButton=tk.Button(root, command=root.destroy)
        AtrasButton["bg"] = "#75FF46"
        ft = tkFont.Font(family='Comics',size=13)
        AtrasButton["font"] = ft
        AtrasButton["fg"] = "#000000"
        AtrasButton["justify"] = "center"
        AtrasButton["text"] = "Atras"
        AtrasButton.place(x=330,y=360,width=91,height=30)
     #  AtrasButton["command"] = self.AtrasButton_command
    
    #def AtrasButton_command(self):
    def creabutacas(self, audi_id): #crea n butacas para audicion.
        for i in (range(self.sala.asientos)):
            butemp=Butaca()
            butemp.sala=self.sala.id
            butemp.numero=i+1
            butemp.audi=audi_id
            butemp.grabar_datos()
            print(f"creando butaca {i+1} en sala id {self.sala.id} tipo {self.sala.tipo}")        
        print (f"creando {self.sala.asientos}")
        print (audi_id)
    
    def GButton_701_command(self):
        audi=Audicion()
        audi.pelicula=self.peli.id
        audi.sala=self.sala.id
        dia=date(int(self.YearAudiBox.get()),int(self.MesAudiBox.get()),int(self.DiaAudiBox.get()))
        hora=time(int(self.HoraAudiBox.get()),int(self.MinAudiBox.get()))
        audi.fecha=dia
        audi.hora=hora
        audi.get_id_db()
        self.creabutacas(audi.id)
        messagebox.showinfo('Confirmación','Datos guardados correctamente')
        
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = AudiAdminMenu(root)
    root.mainloop()