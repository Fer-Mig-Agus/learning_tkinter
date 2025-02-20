import tkinter as tk

window=tk.Tk()
window.title('Ejemplo grid')

window.geometry('400x500+600+300')

# creamos dos lables y los posicionamos con pack
# label1=tk.Label(window,text='Label 1')
# label1.pack()
#
# label2=tk.Label(window,text='Label 1')
# label2.pack()

frame_buttons=tk.Frame(window)
frame_buttons.pack(pady=10)

button1=tk.Button(frame_buttons,text='Boton 1')
button1.pack(side='left', padx=5)
button2=tk.Button(frame_buttons,text='Boton 1')
button2.pack(side='left', padx=5)
button3=tk.Button(frame_buttons,text='Boton 1')
button3.pack(side='left', padx=5)





window.mainloop()



