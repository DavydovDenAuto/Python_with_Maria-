import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
# идентификатор равен 1 для первой фигуры, но его можно получить
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, width=5)

for x in range(0, 20):
    # движение (1 = идентификатор треугольника, 5=dx, 2=dy)
    #canvas.move(1, 5, 2)
    canvas.move(mytriangle , 5, 2) 
    tk.update() #перерисовка
    time.sleep(0.05) 

def movetriangleEnter(event):
    canvas.move(mytriangle, -5, -2)

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.itemconfig(mytriangle, fill='blue') #изменение свойств
        canvas.itemconfig(mytriangle, outline='red')
        canvas.move(mytriangle, 0, -3)
    elif event.keysym == 'Down':
        canvas.itemconfig(mytriangle, fill='red')
        canvas.itemconfig(mytriangle, outline='blue')
        canvas.move(mytriangle, 0, 3)
    elif event.keysym == 'Left':
        canvas.itemconfig(mytriangle, fill='cyan')
        canvas.itemconfig(mytriangle, outline='red')
        canvas.move(mytriangle, -3, 0)
    else:
        canvas.itemconfig(mytriangle, fill='magenta')
        canvas.itemconfig(mytriangle, outline='blue')
        canvas.move(mytriangle, 3, 0)

#<KeyPress-Return> событие нажатия клавиши Enter или Return
canvas.bind_all('<KeyPress-Return>', movetriangleEnter)
# клавиши со стрелками
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
    
