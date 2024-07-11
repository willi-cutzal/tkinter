import tkinter as tk
from tkinter import ttk # tkk es un submódulo de tkinter


def presionar():
    entrada_usuario = (entrada.get())
    
    #actualizando etiqueta
    #etiqueta.config(text="bienvenido de nuevo!!!")
    
    #segunda forma
    etiqueta['text']=entrada_usuario
    entrada['state']='disable'


ventana = tk.Tk()

ventana.title("cuarto programa")

ventana.geometry("1000x800")

etiqueta = ttk.Label(master=ventana, text="hola, bienvenidos")

entrada = ttk.Entry(master=ventana)

boton = ttk.Button(master=ventana, text="presionar", command=presionar)


etiqueta.pack()
entrada.pack()
boton.pack()



ventana.mainloop()