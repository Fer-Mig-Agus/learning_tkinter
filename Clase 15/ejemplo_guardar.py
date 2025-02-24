import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    file_path=filedialog.askopenfilename(filetypes=[('Archivos de texto','*.txt'),('Todos los archivos','*.*')])
    if file_path:
        with open(file_path,'r') as file_obj:
            contenido=file_obj.read()
            text_widget.delete(1.0,tk.END)
            text_widget.insert(tk.INSERT,contenido)


def guardar_archivo():
    file_path=filedialog.askopenfilename(filetypes=[('Archivos de texto','*.txt'),('Todos los archivos','*.*')])
    if file_path:
        with open(file_path,'w') as file_obj:
            contenido=text_widget.get(1.0,tk.END)
            file_obj.write(contenido)


window=tk.Tk()
window.title('Editor de archivo de texto')

text_widget=tk.Text(window,wrap='word')
text_widget.pack(expand=True,fill='both')

abrir_button=tk.Button(window,text='Abrir archivo',command=abrir_archivo)
abrir_button.pack(side='left')

guardar_button=tk.Button(window,text='Guardar archivo',command=guardar_archivo)
guardar_button.pack(side='right')

window.mainloop()




