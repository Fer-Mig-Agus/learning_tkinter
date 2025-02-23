import tkinter as tk



window=tk.Tk()
window.geometry('400x500+600+200')
window.title('Ejemplo de imagenes')

image2=tk.PhotoImage(file='image2.png')
image3=tk.PhotoImage(file='image3.gif')

tag=tk.Label(window,image=image3)
button=tk.Button(window,image=image2)
tag.pack()
button.pack()



window.mainloop()









