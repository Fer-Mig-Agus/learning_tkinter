import tkinter as tk

window=tk.Tk()

window.title('My Frame')
window.geometry('600x400')
window.configure(bg='Lightblue')

# CREACION DE FRAMES
# frame1=tk.Frame(window)
# frame1.configure(width=300,height=200,bg='red',bd=5)
# frame1.pack()
#
# frame2=tk.Frame(frame1)
# frame2.configure(width=100,height=100,bg='blue',bd=5)
# frame2.pack()
#
# button=tk.Button(frame1,text='Hello')
# button.pack()


# CREACION DE LABEL

label_frame=tk.LabelFrame(window,text='Grupo de widgets' , bg='yellow', padx=10, pady=10)
label_frame.configure(width=300,height=200)
label_frame.pack()


window.mainloop()




















