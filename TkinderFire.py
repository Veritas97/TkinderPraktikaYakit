import tkinter as tk
from random import *

window = tk.Tk()
window.title("FifeAndDance")

ROW = 7
COLUMS = 3

buttons = []
for i in range(ROW):
    temp = []
    for j in range(COLUMS):
        btn = tk.Button(window)
        temp.append(btn)
    buttons.append(temp)

for row_btn in(buttons):
    print(row_btn)


window.mainloop()