from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def click(num):
    e.insert(END, num)

def clear():
    e.delete(0, END)

def equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row, col = 1, 0
for b in buttons:
    if b == '=':
        Button(root, text=b, padx=20, pady=20, command=equal).grid(row=row, column=col)
    else:
        Button(root, text=b, padx=20, pady=20, command=lambda x=b: click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text="C", padx=20, pady=20, command=clear).grid(row=row, column=0, columnspan=4, sticky="we")

root.mainloop()
