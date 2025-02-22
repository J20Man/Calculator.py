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
# ttk.Label(symbols, text="Hello World!").grid(column=0, row=0)
ttk.Button(bttns, text="+").grid(column=4, row=1)
ttk.Button(bttns, text="-").grid(column=5, row=1)
ttk.Button(bttns, text="X").grid(column=4, row=2)
ttk.Button(bttns, text="/").grid(column=5, row=2)
ttk.Button(bttns, text="=").grid(column=5, row=3)

def listitems(self, event):
    print(event.widget['text'])

# #defiens the buttons needed for the numbers
# ttk.Button(bttns, text="1").bind("<Button-1>", listitems()).grid(column=1, row=3)
# ttk.Button(bttns, text="2").grid(column=2, row=3)
# ttk.Button(bttns, text="3").grid(column=3, row=3)
# ttk.Button(bttns, text="=").grid(column=5, row=3)
# #row two
# ttk.Button(bttns, text="4").grid(column=1, row=2)
# ttk.Button(bttns, text="5").grid(column=2, row=2)
# ttk.Button(bttns, text="6").grid(column=3, row=2)
# #row three
# ttk.Button(bttns, text="7").grid(column=1, row=1)
# ttk.Button(bttns, text="8").grid(column=2, row=1)
# ttk.Button(bttns, text="9").grid(column=3, row=1)


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