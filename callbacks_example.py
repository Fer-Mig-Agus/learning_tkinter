import tkinter as tk

def on_click(event):
    print(f'Boton {event.widget['text']} precionado')


window=tk.Tk()

window.geometry('400x500+600+300')

buttons={tk.Button(window,text=f"Boton {i}" )for i in range(3)}
for button in buttons:
    button.pack()
    button.bind('<Button-1>',on_click )


window.mainloop()
