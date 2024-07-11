import tkinter as tk

#from tkinter import ttk

import ttkbootstrap as ttk


def convertir():
    entrada_numero = entrada_entera.get()
    
    resultado = entrada_numero * 100
    
    salida_cadena.set(resultado)


# ventana

#ventana = tk.Tk()
#ventana = ttk.Window(themename='darkly')
ventana = ttk.Window(themename='journal')
ventana.title("demo")

ventana.geometry("400x200")  # "ancho X alto"

titulo_etiqueta = ttk.Label(
    master=ventana, text="titulo de etiqueta", font="Calibri 24 bold"
)  # font = "tipo_fuente tamaño estilo"
titulo_etiqueta.pack()

# campo de entrada

marco_entrada = ttk.Frame(master=ventana)
entrada_entera = (
    tk.IntVar()
)  # aquí se guarda lo que ingresamos y abajo se coloca formato etc
entrada = ttk.Entry(master=marco_entrada, textvariable=entrada_entera)
boton = ttk.Button(master=marco_entrada, text="botón para convertir", command=convertir)

# notar que importa el orden en que se empaquetan, boton->entrada no es igual entrada->boton

entrada.pack(
    side="left", padx=5
)  # se agrega la opción side="left" para que queden uno al lado del otro, padx es el espaciado entre ambos objetos horizontalmente
boton.pack(side="left")
marco_entrada.pack(pady=20)


# campo salida
salida_cadena = tk.StringVar()
salida_etiqueta = ttk.Label(
    master=ventana,
    text="etiqueta de salida",
    font="Calibri 15",
    textvariable=salida_cadena,
) #cuando agregamos text variable, ya no aparecerá el text="etiqueta de salida", ahora será dinámico

salida_etiqueta.pack()

# correr_programa
ventana.mainloop()
