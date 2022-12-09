import tkinter as tk
from random import *
class FifeAndDance():
    
    window = tk.Tk()
    window.title("FifeAndDance")
    ROW = 10
    COLUMS = 10

    def __unit__(self):
        self.buttons = []
        for i in range(FifeAndDance.ROW):
            temp = []
            for j in range(FifeAndDance.COLUMS):
                btn = tk.Button(FifeAndDance.window, width=3, font='Calibri 15 bold')
                temp.append(btn)
        self.buttons.append(temp)

    def create_widgets(self):
        for i in range(FifeAndDance.ROW):
            for j in range(FifeAndDance.COLUMS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def start(self):
        FifeAndDance.window.mainloop()

game = FifeAndDance()
game.create_widgets()
game.start()

for row_btn in (game.buttons):
    print(row_btn)