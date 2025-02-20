import tkinter as tk

window=tk.Tk()
window.title('Ejemplo Label')

tag=tk.Label(window,text='Hola, soy un label')

# Si se quiere cambiar el texto del label se hace de esta manera
#tag.configure(text='Nuevo texto')

tag.config(fg='blue',bg='yellow', font=('Arial',12,'italic'))



tag.pack()

window.mainloop()

