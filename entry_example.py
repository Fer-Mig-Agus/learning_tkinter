import tkinter as tk
import time

window=tk.Tk()
window.title('Ejemplo input')
window.title('Ejemplo Label')
window.geometry('500x300+500+300')

tag=tk.Label(window,text='Lo de abajo es un input (entry)')
tag.pack()


input=tk.Entry(window)
input.config(fg='black',bg='yellow', font=('Arial',12,'italic'))
input.pack()
#Esto seria un placeholder
# input.insert(0,'Nombre...')
# texto=input.get()
# print(texto)

def apply_text():
    text_=input.get()
    tag.config(text=text_)

button_apply=tk.Button(window,text='Aplicar texto', command=apply_text)
button_apply.pack()



window.mainloop()

