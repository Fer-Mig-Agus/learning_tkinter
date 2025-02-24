import tkinter as tk



def iniciar_arrastre(event):
    global objeto_selecionado
    objeto_selecionado=canvas.find_closest(event.x,event.y)


def terminar_arrastre(event):
    global objeto_selecionado
    if objeto_selecionado:
        x,y=event.x,event.y
        canvas.move(objeto_selecionado,x-canvas.coords(objeto_selecionado)[0],y-canvas.coords(objeto_selecionado)[1])
        objeto_selecionado=None


window=tk.Tk()
canvas=tk.Canvas(window,width=500,height=300,bg='lightblue')

canvas.pack()

objeto_selecionado=None

rectangulo=canvas.create_rectangle(100,100,200,200,fill='green',outline='black',width=2,tags='rectangulo')

canvas.tag_bind('rectangulo','<ButtonPress-1>',iniciar_arrastre)
canvas.tag_bind('rectangulo','<ButtonRelease-1>',terminar_arrastre)

window.mainloop()