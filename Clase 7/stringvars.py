import tkinter as tk

window=tk.Tk()

window.geometry('400x500+300+400')

#text_=tk.StringVar(value='Hello world')
text_=tk.StringVar()
text_.set('New Text')

#
# print(text_.get())
# print(text_.get())

input=tk.Entry(window,textvariable=text_)
input.pack()

tag=tk.Label(window)
tag.pack()

def update_tag(*args):
    tag.config(text=text_.get())

text_.trace('w',update_tag)


window.mainloop()