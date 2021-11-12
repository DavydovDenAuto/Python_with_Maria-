#Средствами tkinter можно загружать только изображения формата GIF
#Чтобы вывести изображение другого типа, скажем, PNG (.png) или JPG (.jpg),
#придется воспользоваться другим модулем, например Python Imaging Library
#(http://www.pythonware.com/products/pil/).

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image = PhotoImage(file='/Users/dev/Downloads/test.gif')
# anchor=NW означает, что изображение должно выводиться
#с левого верхнего угла (иначе за отправную точку считался бы центр изображения).
canvas.create_image(100, 100, anchor=SE, image=my_image)

tk.mainloop()
