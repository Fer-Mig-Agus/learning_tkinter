import tkinter as tk
from email.policy import default
from tkinter import ttk

window=tk.Tk()
window.geometry('400x500+600+200')
window.title('Ejemplo de combobox')


combobox=ttk.Combobox(window,width=30,font=('Arial',12), foreground='blue',background='white')
combobox.pack()

elements=['Elemento 1','Elemento 2','Elemento 3']
combobox['values']=elements
# # Si queremos eliminar un elemento de la lista lo podemos hacer asi
# elements.remove('Elemento 1')
# #Pero tenemos que actualizar la lista
# combobox['values']=elements


def on_selected(value):
    value_selected=combobox.get()
    print(f'Seleccionado: {value_selected}')


combobox.bind('<<ComboboxSelected>>',on_selected)



window.mainloop()
