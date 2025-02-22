import tkinter as tk
from tkinter import *
from tkinter import ttk

#init the winow
root = Tk()
# root.state("zoomed")
root.title("Calculator")
root.configure(bg="grey")
bttns = ttk.Frame(root, padding=10)

#defines the buttons needed for the calculator
bttns.grid()
display = tk.Label(bttns, text="0", bg="grey").grid(column=0, row=0, columnspan=5)

run = 0
total = 0


def listitems(event):
    # print(event.widget['text'])
    global total 
    num = int(event.widget['text'])
    total += num 
    print(total)
        

symbols = [
    ('+', 4, 1), ('-', 5, 1), ('X', 4, 2),
    ('/', 5, 2), ('=', 5, 3)
]

for num, col, row in symbols:
    btn = ttk.Button(bttns, text=str(num))
    btn.grid(column=col, row=row)
    btn.bind("<Button-1>", listitems)  # Bind the function

# Number Buttons
numbers = [
    (1, 1, 3), (2, 2, 3), (3, 3, 3),
    (4, 1, 2), (5, 2, 2), (6, 3, 2),
    (7, 1, 1), (8, 2, 1), (9, 3, 1)
]

# Create buttons and bind events
for num, col, row in numbers:
    btn = ttk.Button(bttns, text=str(num))
    btn.grid(column=col, row=row)
    btn.bind("<Button-1>", listitems)  # Bind the function

root.mainloop()