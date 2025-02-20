import tkinter as tk

window=tk.Tk()
window.title('Ejemplo check button')

window.geometry('400x500+600+300')


# variable_check_1=tk.BooleanVar()
# variable_check_2=tk.BooleanVar()
#
#
#
# check1=tk.Checkbutton(window,text='Option 1',variable=variable_check_1)
# check2=tk.Checkbutton(window,text='Option 2',variable=variable_check_2)

# check1.pack()
# check2.pack()

# def on_checkbutton_change():
#     print('Checkbutton cambiado')



variable_check_1=tk.BooleanVar()

def enable_button():
    if variable_check_1.get():
        button.config(state='normal')
    else:
        button.config(state='disabled')


check1=tk.Checkbutton(window,text='Habilitar boton',variable=variable_check_1, command=enable_button)
button=tk.Button(window,text='Boton',state='disabled')

check1.pack()
button.pack()




















window.mainloop()
