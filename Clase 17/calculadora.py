import tkinter as tk

window=tk.Tk()
window.geometry('300x400')
window.resizable(False,False)

value_a=0
value_b=0
operation='sumar'
result=0

# Funciones
def sumar():
    global value_a
    global value_b
    return value_a+value_b

def restar():
    global value_a
    global value_b
    return value_a-value_b

def dividir():
    global value_a
    global value_b
    return value_a/value_b

def multiplicar():
    global value_a
    global value_b
    return value_a*value_b


def borrar():
    global screen
    screen.delete(0,tk.END)


def add_to_screen(value:str):
    global screen
    screen.insert(tk.END,value)

def operar(simbolo):
    global screen
    global value_a
    global operation
    value_a=float(screen.get())
    match(simbolo):
        case '/':
            operation='dividir'
        case '*':
            operation = 'multiplicar'
        case '+':
            operation = 'sumar'
        case '-':
            operation = 'restar'

    screen.delete(0,tk.END)


def result_equal():
    global screen
    global value_a
    global value_b
    global result
    global operation

    value_b=float(screen.get())
    screen.delete(0,tk.END)
    evaluacion=eval(operation)
    result=evaluacion()
    screen.insert(tk.END,result)


# Intefaz grafica
    #pantalla

screen=tk.Entry(window, width=39, bd=6,justify='right')
screen.grid(row=0, column=0, columnspan=4)


    #Botones
button_seven=tk.Button(window, text='7', width=7, command=lambda:   add_to_screen(7))
button_seven.grid(row=1,column=0)
button_eight=tk.Button(window, text='8', width=7, command=lambda:   add_to_screen(8))
button_eight.grid(row=1,column=1)
button_nine=tk.Button(window, text='9', width=7, command=lambda:   add_to_screen(9))
button_nine.grid(row=1,column=2)
button_division=tk.Button(window, text='/', width=7, command=lambda: operar('/'))
button_division.grid(row=1,column=3)

button_six=tk.Button(window, text='6', width=7 ,command= lambda: add_to_screen(6))
button_six.grid(row=2,column=0)
button_five=tk.Button(window, text='5', width=7 ,command= lambda: add_to_screen(5))
button_five.grid(row=2,column=1)
button_four=tk.Button(window, text='4', width=7 ,command= lambda: add_to_screen(4))
button_four.grid(row=2,column=2)
button_multiplication=tk.Button(window, text='*', width=7, command=lambda: operar('*'))
button_multiplication.grid(row=2,column=3)

button_three=tk.Button(window, text='3', width=7 ,command= lambda: add_to_screen(3))
button_three.grid(row=3,column=0)
button_two=tk.Button(window, text='2', width=7 ,command= lambda: add_to_screen(2))
button_two.grid(row=3,column=1)
button_one=tk.Button(window, text='1', width=7 ,command= lambda: add_to_screen(1))
button_one.grid(row=3,column=2)
button_subtraction=tk.Button(window, text='-', width=7, command=lambda: operar('-'))
button_subtraction.grid(row=3,column=3)

button_point=tk.Button(window, text='.',width=7 ,command= lambda: add_to_screen('.'))
button_point.grid(row=4,column=0)
button_zero=tk.Button(window, text='0',width=7 ,command= lambda: add_to_screen(0))
button_zero.grid(row=4,column=1)
button_equal=tk.Button(window, text='=',width=7,command=result_equal)
button_equal.grid(row=4,column=2)
button_plus=tk.Button(window, text='+',width=7, command=lambda: operar('+'))
button_plus.grid(row=4,column=3)

button_delete=tk.Button(window, text='Borrar',width=32,command=borrar)
button_delete.grid(row=5,column=0,columnspan=4)

window.mainloop()