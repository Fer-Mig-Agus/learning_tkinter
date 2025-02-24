import tkinter as tk

window=tk.Tk()
window.title('Ejemplo desplazamiento')

window.geometry('400x500+600+300')

scrollbar_horizontal=tk.Scrollbar(window,orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(fill='x')


window.mainloop()