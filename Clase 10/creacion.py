import tkinter as tk
from tkinter.scrolledtext import ScrolledText

window=tk.Tk()
text_=tk.Text(window, width=40, height=10, wrap='word', bg='lightgray',fg='black',pady=10,padx=10,font=('Helvetica',12))
text_.insert('1.0','Bienvenido a nuestro editor de texto')
text_.insert('end','\n\nEste es un ejemplo de texto resaltado','resaltado')
text_.tag_configure('resaltado',background='yellow',foreground='black')
content=text_.get('1.0','end')
#text_.delete('1.0','end')
text_.pack()

texto_desplazable=ScrolledText(window)
texto_desplazable.pack()

window.mainloop()

