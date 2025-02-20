import tkinter as tk


def on_click(event):
    print('Boton precionado')

window=tk.Tk()
window.geometry('500x500+400+300')

button=tk.Button(window,text='Haz click aqui')
button.pack()

#Esto es para que solo se pueda hacer click con el boton izquierdo de mouse
button.bind('<Button-1>', on_click)

#Esto es para que solo se pueda hacer click con el boton de scroll de mouse
#button.bind('<Button-2>', on_click)

#Esto es para que solo se pueda hacer click con el boton derecho de mouse
#button.bind('<Button-3>', on_click)


# Para saber que tecla del teclado preciona
def on_key_press(event):
    if event.char == 'a':
        print('Tecla "a" precionado')


window.bind('<KeyPress>', on_key_press)


# Para redimencionar la ventana
# def on_size(event):
#     print(f'La ventana ha sido redimencionado a {event.width}x{event.height}')
#
#
# window.bind('<Configure>', on_size)


# Para ver donde esta ubicado el mouse
# def on_mouse_move(event):
#     print(f'Mouse movido a {event.x}x{event.y}')
#
# window.bind('<Motion>',on_mouse_move)



window.mainloop()

