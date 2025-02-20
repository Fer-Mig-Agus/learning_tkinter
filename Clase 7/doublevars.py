import tkinter as tk

window=tk.Tk()

window.geometry('400x500+300+400')

decimal=tk.DoubleVar(value=3.14)


control_deslizante=tk.Scale(window,variable=decimal,from_=0,to=100,resolution=0.01,orient=tk.HORIZONTAL)

control_deslizante.pack()


window.mainloop()

doublevars.py