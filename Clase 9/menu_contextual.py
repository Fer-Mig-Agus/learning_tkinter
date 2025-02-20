import tkinter as tk

window=tk.Tk()
window.geometry('400x500+600+200')

def show_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root,event.y_root)

menu_contextual=tk.Menu(window,tearoff=0)
menu_contextual.add_command(label='Cortar')
menu_contextual.add_command(label='Copiar')
menu_contextual.add_command(label='Pegar')


input=tk.Entry(window)
input.pack()

input.bind('<Button-3>',show_menu_contextual)

window.mainloop()














