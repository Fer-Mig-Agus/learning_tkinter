import tkinter as tk

window=tk.Tk()
window.title('Ejemplo desplazamiento')

window.geometry('400x500+600+300')

texto=tk.Text(window)

scrollbar_vertical=tk.Scrollbar(window)
scrollbar_vertical.pack(side='right',fill='y')


scrollbar_vertical.config(command=texto.yview)
texto.config(yscrollcommand=scrollbar_vertical.set)
texto.pack(side='left', fill='both',expand=True)


window.mainloop()