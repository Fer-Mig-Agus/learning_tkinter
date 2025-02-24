import tkinter as tk

window=tk.Tk()
window.title('Ejemplo desplazamiento')

window.geometry('400x500+600+300')

scrollbar_vertical=tk.Scrollbar(window)
scrollbar_vertical.pack(side='right',fill='y')


window.mainloop()