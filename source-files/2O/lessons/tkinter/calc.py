from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Калькулятор')
        self.settings()
        self.tk.update()

    def settings(self):
        self.frame1 = Frame(self.tk)
        self.frame1.pack()
        self.frameButtons = Frame(self.tk)
        self.frameButtons.pack()
        self.frameResults = Frame(self.tk)
        self.frameResults.pack()
        self.A = DoubleVar()
        self.A.set(5.2)
        self.B = DoubleVar()
        self.B.set(10.2)
        self.Result = DoubleVar()
        self.Result.set(0)

        lable1 = ttk.Label(self.frame1, text='a = ')
        lable1.pack(side = LEFT)
        entry1 = ttk.Entry(self.frame1, textvariable = self.A)
        entry1.pack(side=LEFT)

        lable2 = ttk.Label(self.frame1, text='b = ')
        lable2.pack(side=LEFT)
        entry2 = ttk.Entry(self.frame1, textvariable=self.B)
        entry2.pack(side=LEFT)



    def mainloop(self):
        self.tk.mainloop()


g = Calculator()
g.mainloop()

