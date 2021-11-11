from tkinter import *
from tkinter import colorchooser #т.к. нет в списке
import random

tk = Tk()
canvas = Canvas(tk, width=700, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500 ) #координаты начала и конца
canvas.create_rectangle(10, 100, 50, 250) #координаты левого верхнего и правого нижнего угла 

def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

random_rectangle(400, 400, 'red')
random_rectangle(400, 400, '#ffd800')
my_color = colorchooser.askcolor() # ((0.0, 255.99609375, 0.0), '#00ff00')
random_rectangle(400, 400, my_color[1])

# дуга (координаты углов прямоугольника, в который вписана,
# extent = угол разворота дуги в градусах от Ox против часовой стрелки
# style = сектор PIESLICE (по умолчанию), сегмент (CHORD) или дугу (ARC).
# В качестве полного оборота используем угол 359 градусов, а не 360, 
# tkinter считает, что угол 360 градусов = 0 градусов, и ничего не нарисует.
# 
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC, width=5)
canvas.create_arc(50, 50, 190, 190, start=240, extent=100, style=CHORD, fill='green')
canvas.create_arc(250, 10, 190, 190, start=45, extent=100, style=PIESLICE, fill='magenta')

#Polygon — многоугольник  Outline — контур
#tkinter автоматически замкнет контур, проведя линию к первой точке 
canvas.create_polygon(310, 310, 400, 210, 450, 320, fill="", outline="red")
# текст
canvas.create_text(130, 120, text='арбуз', fill='red', font=('Times', 15) )
# anchor - По умолчанию в заданной координате располагается
# центр текстовой надписи. Чтобы изменить это, используется якорь
# W (от англ. west – запад) = разместить по указанной координате левую границу текста
# Другие значения: N, NE, E, SE, S, SW, W, NW.
# Если букв, задающих сторону привязки, две, то вторая определяет
# вертикальную привязку (вверх или вниз «уйдет» текст от заданной координаты).
# Свойство justify определяет лишь выравнивание текста относительно себя самого. 
canvas.create_text(400, 200, text="Hello World,\nPython\nand Tk", 
                justify=CENTER, font="Verdana 24",
                anchor=SW, fill="green")
#ellips
canvas.create_oval(10, 10, 25, 25)