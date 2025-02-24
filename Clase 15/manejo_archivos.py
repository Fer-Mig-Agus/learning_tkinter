import tkinter as tk
from tkinter import filedialog

window=tk.Tk()
window.withdraw()

file_path=tk.filedialog.askopenfilename()
print(file_path)

file_obj=filedialog.askopenfile(mode='r')
if file_obj:
    print(file_obj.read())
    file_obj.close()

file_paths=filedialog.askopenfilenames()
print(file_paths)

file_obj2=filedialog.askopenfile(mode='r')
if file_obj2:
    print(file_obj2.read())
    file_obj2.close()


window.mainloop()