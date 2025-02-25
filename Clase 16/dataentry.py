import tkinter as tk
from tkcalendar import DateEntry


window=tk.Tk()
window.geometry('500x300')

date_entry=DateEntry(window)
date_entry.pack()

date_entry.bind('<<DateEntrySelected>>',lambda e: print(date_entry.get()))

window.mainloop()

