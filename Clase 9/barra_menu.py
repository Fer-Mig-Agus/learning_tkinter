import tkinter as tk

window=tk.Tk()
window.geometry('400x500+600+200')


barra_menu=tk.Menu(window)
window.config(menu=barra_menu)

#Añadimos el boton Archivo
archive_menu=tk.Menu(barra_menu)
barra_menu.add_cascade(label='Archivo',menu=archive_menu)

archive_menu.add_command(label='Nuevo')
archive_menu.add_command(label='Abrir')
archive_menu.add_separator()
archive_menu.add_command(label='Salir')

#Añadimos el boton Editar
editar_menu=tk.Menu(barra_menu)
barra_menu.add_cascade(label='Editar', menu=editar_menu)

editar_menu.add_command(label='Deshacer')
editar_menu.add_command(label='Rehacer')




window.mainloop()