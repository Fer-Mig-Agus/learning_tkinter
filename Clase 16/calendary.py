import tkinter as tk
from tkcalendar import Calendar

window=tk.Tk()
# Por defecto el calendario esta en formato ingles
#cal=Calendar(window)

#Para colocarlo en spanish de hace de esta manera
cal=Calendar(window,selectmode='day',locale='es_ES',year=2023,month=7,day=1,date_pattern='y-mm-dd')

cal.pack()

def print_date(date):
    print(date)

cal.bind('<<CalendarSelected>>',lambda e: print_date(cal.get_date()))




window.mainloop()