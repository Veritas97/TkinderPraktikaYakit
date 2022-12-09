import tkinter as tk
from random import *

class Fife:
    
    window = tk.Tk()
    ROW = 10
    COLUMS = 10
    
    def __init__(self):
        self.buttons = []
        for i in range(Fife.ROW):
            temp = []
            for j in range(Fife.COLUMS):
                btn = tk.Button(Fife.window, width=3, font='Calibri 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(Fife.ROW):
            for j in range(Fife.COLUMS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def start(self):
        self.create_widgets()
        self.print_buttons()
        Fife.window.mainloop()


game = Fife()
game.start()
