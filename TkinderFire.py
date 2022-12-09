import tkinter as tk

win = tk.Tk()
ROW = 10
COLUMNS = 7

buttons = []
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = tk.Button(win, width=3, font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

for row_btn in buttons:
    print(row_btn)

for i in range(ROW):
    for j in range(COLUMNS):
        btn = buttons[i][j]
        btn.grid(row=i, columns=j)
    
win.mainloop()