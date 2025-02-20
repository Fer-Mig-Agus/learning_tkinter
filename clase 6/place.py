import tkinter as tk

window=tk.Tk()
window.title('Ejemplo grid')

window.geometry('400x500+600+300')

# Creamos dos labels y los posicionamos con place
label1=tk.Label(window,text='Label 1')
label1.place(x=50 ,y=50)

label2=tk.Label(window,text='Label 2')
label2.place(x=100 ,y=100)

#Se puede usar coordenadas relativas que seria como el porcentaje

label3=tk.Label(window,text='Label 3')
label3.place(relx=0.50 ,rely=0.10)


window.mainloop()