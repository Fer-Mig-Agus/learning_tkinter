import tkinter as tk
from tkinter import filedialog

window=tk.Tk()
window.withdraw()

file_obj=filedialog.asksaveasfile(mode='w',defaultextension='.text')
if file_obj:
    file_obj.write('Hola mundo! aiuuuuuu')
    file_obj.close()

