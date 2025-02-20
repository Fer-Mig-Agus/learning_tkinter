import tkinter as tk

window=tk.Tk()
window.title('Ejemplo grid')

window.geometry('400x500+600+300')

# creamos dos lables y los posicionamos con grid
label1=tk.Label(window,text='Label 1,1')
label1.grid(row=0,column=0, padx=5,pady=5)
label2=tk.Label(window,text='Label 1,2')
label2.grid(row=0,column=1, padx=5,pady=5)
label2=tk.Label(window,text='Label 2,1')
label2.grid(row=1,column=0, padx=5,pady=5)
label2=tk.Label(window,text='Label 2,2')
label2.grid(row=1,column=1, padx=5,pady=5)



window.mainloop()


