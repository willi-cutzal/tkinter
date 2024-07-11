import tkinter as tk

import ttkbootstrap as ttk

# ***   funciones   ***

def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if type(numero) != int or numero < 0: return None
    elif numero == 0: return 0
    binario = ''
    div_resto = 0
    while numero > 0:
        div_resto = numero % 2
        # numero = numero // 2
        numero //= 2
        binario += str(div_resto)
    return int(binario[::-1])

def binarier():
    entrada_numero = entrada_entera.get()
    resultado = NumeroBinario(entrada_numero)
    salida_var.set(resultado)




# ***   ventana   ***

ventana = ttk.Window(
    title="calculadora", themename="journal", iconphoto="ninja_serio.png"
)

# ***   dimensiones   ***
ventana.geometry("400x400")


# ***   etiquetas   ***

# ***   Bienvenida   ***
bienvenida = ttk.Label(master=ventana, text="Bienvenido!!!", font="System 24 bold")
bienvenida.pack()


# ***   marco   ***
marco_entrada = ttk.Frame(master=ventana)

# ***   widgets en marco   ***
entrada_entera = tk.IntVar()
entrada = ttk.Entry(master=marco_entrada, textvariable=entrada_entera)

boton = ttk.Button(master=marco_entrada, text="convertir", command=binarier)

salida_var = tk.StringVar()
salida_etiqueta = ttk.Label(master=marco_entrada, font="Calibri 15", textvariable=salida_var)


# ***   empaquetado   ***
entrada.pack(side="left", padx=5)
boton.pack(side="left", padx=5)
salida_etiqueta.pack(side="left", padx=10)
marco_entrada.pack(pady=20)


# ***   salida   ***



#correr

ventana.mainloop()