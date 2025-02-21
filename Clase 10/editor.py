from tkinter import Button,Tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename,asksaveasfilename



def open_file():
    file_=askopenfilename()
    if file_:
        texto_desplazable.delete(1.0,'end')
        with open(file_,'r') as file:
            texto_desplazable.insert(1.0,file.read())

def save_file():
    file_=asksaveasfilename()
    if file_:
        with open(file_,'w') as file:
            file.write(texto_desplazable.get(1.0,'end'))

window=Tk()
window.geometry('400x500+600+200')

texto_desplazable=ScrolledText(window,wrap='word')
texto_desplazable.pack(expand=True,fill='both')

button_open=Button(window,text='Open',command=open_file)
button_open.pack(side='left')

button_save=Button(window,text='Save', command=save_file)
button_save.pack(side='left')

window.mainloop()

