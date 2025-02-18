import tkinter as tk

#Creo una instancia de la clase para crear la ventana
window=tk.Tk()

# Para colocar le titulo a la ventana
window.title('Hola chivo')
# Especificamos el tamaño de la ventana
window.geometry('900x500')

#Especificamos un tamaño minimo para la ventana
window.minsize(400,300)
#Especificamos un tamaño maximo para la ventana
window.maxsize(1000,600)

# Mantiene la ventana abierta
window.mainloop()

