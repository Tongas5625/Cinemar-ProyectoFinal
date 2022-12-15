from tkinter import Tk, Label, Button, Entry

ventana = Tk()
ventana.title('calculadora')
# con geometry() damas ancho y altura
ventana.geometry("400x300")
# creamos un label
# creamos la funcion suma
# Al text1 con get le decimos que nos guarde en la n1 y n2


def fnSuma():
    n1 = text1.get()
    n2 = text2.get()
    r = (float(n1) + float(n2))
    # con insert a partir de la pos 0 insertamos el resultado
    # primero deletea,os la caja 3
    text3.delete(0, "end")
    text3.insert(0, r)


lb1 = Label(ventana, text="Primer numero :", bg="pink")
# le damos ancho y altura al label
lb1.place(x=10, y=10, width=100, height=30)
# creamos texto con Enrty
text1 = Entry(ventana, bg="#AEEA99")
text1.place(x=120, y=10, width=100, height=30)

lb2 = Label(ventana, text="Segundo numero :", bg="pink")
lb2.place(x=10, y=50, width=100, height=30)

text2 = Entry(ventana, bg="#AEEA99")
text2.place(x=120, y=50, width=100, height=30)


lb3 = Label(ventana, text="Resultado :", bg="pink")
lb3.place(x=10, y=120, width=100, height=30)

text3 = Entry(ventana, bg="#86DDA4")
text3.place(x=120, y=120, width=100, height=30)
# creacion de boton sumar y cuando se presione se ejec.una funcion suma
but1 = Button(ventana, text="Sumar", command=fnSuma)
but1.place(x=230, y=50, width=80, height=30)


ventana.mainloop()
