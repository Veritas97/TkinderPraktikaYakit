import tkinter as tk
from random import *


class MyButton(tk.Button):

    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.is_earth = False

    def __repr__(self):
        return f"EmptuBtn: {self.x}|{self.y}"
class Fife:

    window = tk.Tk()
    window.title("Огонь бежит")
    ROW = 7
    COLUMS = 10

    def __init__(self):
        self.buttons = []
        for i in range(Fife.ROW):
            temp = []
            for j in range(Fife.COLUMS):
                btn = MyButton(Fife.window, x = i, y = j)

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
