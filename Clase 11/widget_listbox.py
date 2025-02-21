import tkinter as tk

window=tk.Tk()
window.geometry('400x500+600+200')
window.title('Ejemplo de listbox')

# Para seleccionar mas de un elemento podemos usar: , selectmode=tk.MULTIPLE
listbox=tk.Listbox(window,width=30, height=10,font=('Arial',12),fg='blue',bg='white')
listbox.insert(tk.END,'Elemento 1')
listbox.insert(tk.END,'Elemento 2')
listbox.insert(tk.END,'Elemento 3')
listbox.insert(0,'Elemento 4')
listbox.insert(1,'Elemento 5')

# listbox.delete(2)
# listbox.delete(0)


def on_seleccionar(event):
    index=listbox.curselection()
    element=listbox.get(index)
    print(f'Selecionado {element}')

def on_click(event):
    print('Click en el Listbox')

def on_double_click(event):
    print('Doble click en el Listbox')

listbox.bind('<<ListboxSelect>>', on_seleccionar)
listbox.bind('<Button-1>',on_click)
listbox.bind('<Double-Button-1>',on_double_click)


listbox.pack()

window.mainloop()
