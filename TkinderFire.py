import tkinter as tk
from random import shuffle

class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_earth = False
        self.is_green = False
        self.is_dry = False

    def __repr__(self):
        return f"Btn: {self.x}|{self.y}|{self.number}|{self.is_earth}|{self.is_green}|{self.is_dry}"
class Fire:

    window = tk.Tk()
    window.title("Огонь бежит")
    ROW = 8
    COLUMS = 8
    EARTH = 5
    GREEN_GRASS = 18
    DRY_GRASS = 18

    def __init__(self):
        self.buttons = []
        count = 1
        for i in range(Fire.ROW):
            temp = []
            for j in range(Fire.COLUMS):
                btn = MyButton(Fire.window, x = i, y = j, number=count)
                btn.config(command=lambda btnFire=btn: self.click(btnFire))
                temp.append(btn)
                count += 1
            self.buttons.append(temp)
    
    def click(self,clicked_btn:MyButton):
        print(clicked_btn)
        if clicked_btn.is_earth:
            clicked_btn.config(text="*", background="red")
        else:
            clicked_btn.config(text=clicked_btn.number)


    def create_widgets(self):
        for i in range(Fire.ROW):
            for j in range(Fire.COLUMS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    def start(self):
        self.create_widgets()
        self.inset_earth()
        self.inset_green()
        self.inset_dry()
        self.print_buttons()
        print(self.get_place_earth())
        print(self.get_place_green())
        print(self.get_place_dry())
        Fire.window.mainloop()
    
    def inset_earth(self):
        place_earth = self.get_place_earth()
        print(place_earth)
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in place_earth:
                    btn.is_earth = True
    
    def inset_green(self):
        place_green = self.get_place_green()
        print(place_green)
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in place_green:
                    btn.is_green = True
    
    def inset_dry(self):
        place_dry = self.get_place_dry()
        print(place_dry)
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in place_dry:
                    btn.is_dry = True

    def get_place_earth(self):
        place = list(range(1, Fire.COLUMS * Fire.ROW + 1))
        shuffle(place)
        return place[:Fire.EARTH]

    def get_place_green(self):
        place = list(range(1, Fire.COLUMS * Fire.ROW + 2))
        shuffle(place)
        return place[:Fire.GREEN_GRASS]

    def get_place_dry(self):
        place = list(range(1, Fire.COLUMS * Fire.ROW + 3))
        shuffle(place)
        return place[:Fire.DRY_GRASS]


game = Fire()
game.start()
