import tkinter as tk
from tkinter import filedialog

#Funciones Call Back

def new_file():
    text_area.delete(1.0,tk.END)

def open_file():
    global file_path
    file_path=filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Archivos de texto', '*.txt'),
                                                                             ('Archivos de python','*.py'),
                                                                             ('Todos los archivos','*.*'), ])
    text_area.delete(1.0,tk.END)
    with open(file_path,'r',encoding='utf-8') as file:
        text_area.insert(tk.INSERT,file.read())



def save_file():
    global file_path
    if file_path:
        try:
            with open(file_path,'w',encoding='utf-8') as file:
                file.write(text_area.get(1.0,tk.END))
        except Exception as e:
            print(f'Hubo un error : {e}')


def save_as_file():
    new_path=filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Archivos de texto', '*.txt'),
                                                                             ('Archivos de python','*.py'),
                                                                             ('Todos los archivos','*.*'), ])
    if new_path:
        with open(new_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))



def copy_text():
    text_area.event_generate(('<<Copy>>'))

def paste_text():
    text_area.event_generate(('<<Paste>>'))


def cut_text():
    text_area.event_generate(('<<Cut>>'))

def show_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root,event.y_root)


window=tk.Tk()
window.title('Block de notas - MF Dev')
window.geometry('800x600+500+200')
window.minsize(400,300)
window.maxsize(1000,600)

window.iconbitmap('logo.ico')

file_path= ''


menu=tk.Menu(window)
window.config(menu=menu)

archivo=tk.Menu(menu)
menu.add_cascade(label='Archivo', menu=archivo)

edicion=tk.Menu(menu)
menu.add_cascade(label='Edicion', menu=edicion)
#,wrap='word'
text_area=tk.Text(window,wrap='word')
text_area.pack(fill=tk.BOTH, expand=True)

archivo.add_command(label='Nuevo',command=new_file)
archivo.add_command(label='Abrir',command=open_file)
archivo.add_command(label='Guardar',command=save_file)
archivo.add_command(label='Guardar como',command=save_as_file)

edicion.add_command(label='Copiar',command=copy_text)
edicion.add_command(label='Pegar',command=paste_text)
edicion.add_command(label='Cortar',command=cut_text)


# Menu contextual
menu_contextual=tk.Menu(window,tearoff=0)
menu_contextual.add_command(label='Copiar' , command=copy_text)
menu_contextual.add_command(label='Cortar' , command=cut_text)
menu_contextual.add_command(label='Pegar' , command=paste_text)

text_area.bind('<Button-3>',show_menu_contextual)










window.mainloop()



























