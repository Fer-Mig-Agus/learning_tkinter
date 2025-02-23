import tkinter as tk
#Esta libreria me permite traer los otros formatos de imagenes
from PIL import Image, ImageTk


window=tk.Tk()
window.geometry('400x500+600+200')
window.title('Ejemplo de imagenes')

tag=tk.Label(window)

image_pil=Image.Open('image1.jpg')
#Tambien puedo redimencionar la imagen
image_resize=image_pil.resize((50,50))
#Tammbien podemos rotar la imagen
image_rotate=image_resize.rotate(90)

image_tk=ImageTk.PhotoImage(image_pil)

button=tk.Button(window,image=image_tk)
button.pack()

window.mainloop()