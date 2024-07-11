import tkinter as tk
from tkinter import font

fuentes = []

root = tk.Tk()
for font in font.families():
    fuentes.append(font)




root.title("ejemplo de fuentes")


for font in fuentes:
    label = tk.Label(root, text=f"{font}", font=(font, 14))
    label.pack()

root.mainloop()