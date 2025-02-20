import tkinter as tk

window=tk.Tk()

window.geometry('400x500+300+400')

boolean=tk.BooleanVar(value=True)


casilla=tk.Checkbutton(window,text='Aceptar', variable=boolean)
casilla.pack()


def update(*args):
    print(boolean.get())

boolean.trace('w',update)

window.mainloop()
