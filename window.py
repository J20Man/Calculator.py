import tkinter as tk
from tkinter import *
from tkinter import ttk

#init the winow
root = Tk()
root.title("Calculator")
root.configure(bg="grey")
root.geometry('400x520')
bttns = ttk.Frame(root, padding=10,)
bttns.grid()

#display the lables
display = tk.Label(bttns, text="0", bg="grey")
display.grid(column=0, row=1, columnspan=6)

prev_display = tk.Label(bttns, text="0", bg="light grey")
prev_display.grid(column=0, row=0, columnspan=6)

#variables needed for calculations
total = ""
first_num = 0
second_num = 0
operator = ""

#functions to handle buttons
def combine_digits(event):
    # print(event.widget['text'])
    global total 
    num = str(event.widget['text'])

    if len(total) < 8:
        total += num 
        display.config(text=total)
    else:
        print("Limit Reached")

def set_operator(event):
    global first_num
    global operator
    global total

    if total:
        first_num = int(total)
        operator = event.widget['text']
        total = ""
        prev_display.config(text=str(first_num) + " " + operator)

def calculate_result(event):
    global first_num
    global second_num
    global total
    global operator

    if total:
        second_num = int(total)
        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "X":
            result = first_num * second_num
        elif operator == "/":
            if second_num != 0:
                result = first_num / second_num
            else:
                result = "Error"
        display.config(text=str(result))
        prev_display.config(text="")

        #clear for next calc
        first_num = result
        total = ""
        operator = ""

def clear_all(event):
    global first_num
    global second_num
    global total
    global operator

    first_num = 0
    second_num = 0
    total = ""
    operator = ""
    display.config(text="0")
    prev_display.config(text="")
       
#Symbols for the buttons
symbols = [
    ('+', 4, 2), ('-', 5, 2), ('X', 4, 3),
    ('/', 5, 3), ('=', 5, 4), ('C', 4, 4)
]

for num, col, row in symbols:
    btn = ttk.Button(bttns, text=str(num),)
    btn.grid(column=col, row=row)
    if num == "=":
        btn.bind("<Button-1>", calculate_result)
    elif num == "C":
        btn.bind("<Button-1>", clear_all)
    else:
        btn.bind("<Button-1>", set_operator)
    

# Number Buttons
numbers = [
    (1, 1, 4), (2, 2, 4), (3, 3, 4),
    (4, 1, 3), (5, 2, 3), (6, 3, 3),
    (7, 1, 2), (8, 2, 2), (9, 3, 2), (0, 1, 5)
]

# Create buttons and bind events
for num, col, row in numbers:
    btn = ttk.Button(bttns, text=str(num))
    btn.grid(column=col, row=row)
    btn.bind("<Button-1>", combine_digits)  

root.mainloop()