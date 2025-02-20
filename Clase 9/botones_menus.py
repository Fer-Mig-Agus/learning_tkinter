import tkinter as tk

window=tk.Tk()
window.geometry('400x500+600+200')
menu_button=tk.Menubutton(window,text='Archivo')
menu_button.pack()


menu=tk.Menu(menu_button)
menu_button.config(menu=menu)

def open_archive():
    print('Archivo abierto')

menu.add_command(label='Abrir',command=open_archive)
menu.add_command(label='Guardar')



window.mainloop()