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
#Coloco el icono que se va a mostrar en ventana
window.iconbitmap('logo.ico')

#Para el color de fondo de la ventana usamos
window.configure(bg='deep sky blue')

#Para bloquear el tamaño de la pantalla
window.resizable(False,False)

#Para cambiar la opacidad
window.attributes('-alpha',0.7)

# Mantiene la ventana abierta
window.mainloop()

