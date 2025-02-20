import tkinter as tk

window=tk.Tk()

window.geometry('400x500+300+400')

integer_=tk.IntVar(value=42)

print(integer_.get())

option1=tk.Radiobutton(window,text='Option 1',font=('Arial',12,'italic'),variable=integer_, value=1, fg='blue', bg='lightgray')
option2=tk.Radiobutton(window,text='Option 2',font=('Arial',12,'italic'),variable=integer_, value=2,  fg='blue', bg='lightgray')

option1.pack()
option2.pack()

def update(*args):
    print(integer_.get())


integer_.trace('w',update)

window.mainloop()

