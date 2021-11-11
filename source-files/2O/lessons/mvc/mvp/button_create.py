from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import random
import time

#    IntVar    BooleanVar    DoubleVar	StringVar
#    get(): возвращает значение self.string_var1.get()
#    set(str): устанавливает значение self.int_var1.set(20) 



class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Кнопки")
        self.game_settings()
        self.tk.update()

    def game_settings(self):
        self.frame1 = Frame(self.tk, relief=RAISED, borderwidth=1 )
        self.frame1.pack( fill="none", expand=True)
        self.frame2 = Frame(self.tk, relief=RAISED, borderwidth=1 )
        self.frame2.pack( fill="none", expand=True)
        #
        self.string_var1 = StringVar() 
        self.string_var1.set("enter text") 
        lab1 = ttk.Label(self.frame1, text="StringVar")
        lab1.pack(side = LEFT, anchor ="nw")
        entry1 = ttk.Entry(self.frame1, textvariable = self.string_var1, width=25)
        entry1.pack(side = LEFT, anchor ="nw")
        #
        self.int_var1 = IntVar()
        self.int_var1.set(20) 
        lab2 = ttk.Label(self.frame1, text="IntVar")
        lab2.pack(side = LEFT, anchor ="nw")
        entry2 = ttk.Entry(self.frame1, textvariable = self.int_var1, width=5)
        entry2.pack(side = LEFT, anchor ="nw")
        #
        btn1 = Button(
            self.frame1, text="print var", command=self.print_var)
        btn1.pack(side = LEFT, padx=10 ) # показ кнопки        
        #
        self.btn_list=[]
        n = len(self.btn_list) 

        btn2 = Button(
            self.frame2, text="add Button", command=self.add_btn)
        btn2.pack(side = LEFT, padx=10 ) # показ кнопки

        self.btn_list.append( btn2 )
        
    def print_var(self):
        print (type(self.string_var1), "self.string_var1 = ", self.string_var1.get())
        print (type(self.int_var1), "self.int_var1 = ", self.int_var1.get())
        print ("len(self.btn_list) = ", len(self.btn_list) )
    
    def add_btn(self):
        n = len(self.btn_list) 
        self.btn_list.append( Button(
            self.frame2, text="btn{0}".format(n), command=self.add_btn))
        self.btn_list[n].pack( side = LEFT, padx=10 )
        #self.tk.update()

    def mainloop(self):
        #обработка нажатий кнопок и клавиш
        self.tk.mainloop()
       

        
# start
g = Game()
g.mainloop()
