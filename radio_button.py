import tkinter as tk

window=tk.Tk()
window.title('Ejemplo radio button')

window.geometry('400x500+600+300')

variable_control=tk.IntVar()

def change_color_window():
    color_selected=variable_control.get()
    if color_selected == 1:
        window.config(bg='red')
    else:
        window.config(bg='blue')

option1=tk.Radiobutton(window,text='Volver rojo',font=('Arial',12,'italic'),variable=variable_control, value=1, command=change_color_window, fg='blue', bg='lightgray')
option2=tk.Radiobutton(window,text='Volver azul',font=('Arial',12,'italic'),variable=variable_control, value=2, command=change_color_window, fg='blue', bg='lightgray')

option1.pack()
option2.pack()

def show_selection():
    print(f'Opcion seleccionado: {variable_control.get()}')

# button=tk.Button(window,text='Mostrar Seleccion', command=show_selection)
# button.pack()






window.mainloop()