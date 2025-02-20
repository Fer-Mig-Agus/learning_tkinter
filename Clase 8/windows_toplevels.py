import tkinter as tk
from tkinter import Toplevel, Label

window=tk.Tk()

window.title('Main Window')
window.geometry('600x400')

# def show_window_toplevel():
#     window_toplevel=Toplevel(window)
#     window_toplevel.title('Toplevel window')
#     window_toplevel.geometry('300x200+50+50')
#     label=Label(window_toplevel,text='Toplevel window')
#     label.pack()


window_toplevel=Toplevel(window)
window_toplevel.title('Toplevel window')
window_toplevel.geometry('300x200+50+50')
label=Label(window_toplevel,text='Toplevel window')
label.pack()

def close_window_toplevel(windows):
    windows.destroy()


# button=tk.Button(window,text='Open Toplevel window',command=show_window_toplevel)
# button.pack()


button_open=tk.Button(window,text='Close Toplevel window',command=lambda : close_window_toplevel(window_toplevel))
button_open.pack()

window.mainloop()