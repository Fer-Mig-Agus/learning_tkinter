import tkinter as tk

def copiar():
    text_.event_generate('<<Copy>>')

def cortar():
    text_.event_generate('<<Cut>>')

def pegar():
    text_.event_generate('<<Paste>>')


window=tk.Tk()
window.geometry('400x500+600+200')

text_=tk.Text(window)
text_.pack()

button_copiar=tk.Button(window,text='Copiar', command=copiar)
button_copiar.pack()

button_cortar=tk.Button(window,text='Cortar', command=cortar)
button_cortar.pack()

button_pegar=tk.Button(window,text='Pegar', command=pegar)
button_pegar.pack()

window.mainloop()
