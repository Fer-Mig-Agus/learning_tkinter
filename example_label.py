import time
import tkinter as tk

window=tk.Tk()
window.title('Ejemplo Label')
window.geometry('500x300+500+300')
tag=tk.Label(window,text='Hola soy un label')

tag.pack()

def actulizar_hora():
    tag.config(text=time.strftime("%H:%M:%S"))
    tag.after(1000, actulizar_hora)


actulizar_hora()

window.mainloop()
