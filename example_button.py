import tkinter as tk
import time

window=tk.Tk()
window.title('Ejemplo boton')
window.geometry('200x400')

button=tk.Button(window,text='Soy un boton')
button.config(fg='white',bg='green',font=('Arial',12))

button.pack()

tag=tk.Label(window,text='etiqueta emergente')
tag.pack()

# def button_click():
#     print('Boton precionado')
#
# button.config(command=button_click)

def change_text():
    tag.config(text='Boton precionado')

button.config(command=change_text)
window.mainloop()

