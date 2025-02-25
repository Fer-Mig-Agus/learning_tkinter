import os
import tkinter as tk
from tkinter import filedialog

def seleccionar_directorio():
    dir_path=filedialog.askdirectory()
    if dir_path:
        listbox.delete(0,tk.END)
        for file in os.listdir(dir_path):
            listbox.insert(tk.END,file)


window=tk.Tk()
window.geometry('400x500+600+200')
window.title('Navegador de archivos')

listbox=tk.Listbox(window)
listbox.pack(expand=True,fill='both')

seleccionar_button=tk.Button(window,text='Seleccionar directorio',command=seleccionar_directorio)
seleccionar_button.pack()

window.mainloop()















