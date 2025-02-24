import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(window,width=500,height=300,bg='lightblue')

rectangulo=canvas.create_rectangle(50,50,150,100,fill='green',outline='black',width=2,tags='rentagulo')

canvas.move(rectangulo,100,100)

canvas.create_oval(200,50,300,150,fill='blue',outline='black',width=2)
canvas.create_polygon(350,50,400,100,350,150, fill='purple',outline='black',width='2')
canvas.create_line(10,200,100,200,fill='orange',width=5,dash=(5,2), capstyle='round')

imagen=tk.PhotoImage(file='imagen.png')
canvas.create_image(150,200,image=imagen, anchor='nw')

imagen_escalada=imagen.subsample(2,2)
canvas.create_image(300,200, image=imagen_escalada,anchor='center', tags='imagen1')















canvas.pack()

window.mainloop()