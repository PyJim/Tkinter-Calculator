from tkinter import *
root = Tk()
root.config(bg="#FFFF00")
root.title("PyJim Calculator")
screen = Entry(root, width="35", borderwidth="5")
screen.grid(row="0", column="0", columnspan="3", padx="10", pady="10")
def button_click(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))
    return
def button_clear():
    screen.delete(0, END)
    return
def button_add():
    first_number = screen.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    screen.delete(0, END)
    return
def button_subtract():
    first_number = screen.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    screen.delete(0, END)
    return
def button_multiply():
    first_number = screen.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    screen.delete(0, END)
    return
def button_divide():
    first_number = screen.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    screen.delete(0, END)
    return

def button_equal():
    second_number = screen.get()
    screen.delete(0, END)
    if math == "addition":
        answer = f_num + float(second_number)
    if math == "subtraction":
        answer = f_num - float(second_number)
    if math == "multiplication":
        answer = f_num * float(second_number)
    if math == "division":
        answer = f_num / float(second_number)
    screen.insert(0, answer)

    

button_1 = Button(root, text="1", padx="40", pady="20", command = lambda:button_click(1)).grid(row="3", column="0")
button_2 = Button(root, text="2", padx="40", pady="20", command = lambda:button_click(2)).grid(row="3", column="1")
button_3 = Button(root, text="3", padx="40", pady="20", command = lambda:button_click(3)).grid(row="3", column="2")

button_4 = Button(root, text="4", padx="40", pady="20", command = lambda:button_click(4)).grid(row="2", column="0")
button_5 = Button(root, text="5", padx="40", pady="20", command = lambda:button_click(5)).grid(row="2", column="1")
button_6 = Button(root, text="6", padx="40", pady="20", command = lambda:button_click(6)).grid(row="2", column="2")

button_7 = Button(root, text="7", padx="40", pady="20", command = lambda:button_click(7)).grid(row="1", column="0")
button_8 = Button(root, text="8", padx="40", pady="20", command = lambda:button_click(8)).grid(row="1", column="1")
button_9 = Button(root, text="9", padx="40", pady="20", command = lambda:button_click(9)).grid(row="1", column="2")

button_0 = Button(root, text="0", padx="40", pady="15", command = lambda:button_click(0)).grid(row="4", column="0")

button_add = Button(root, text="+", padx="40", pady="15", command =button_add).grid(row="6", column="0")
button_equal = Button(root, text="=", padx="90", pady="15", command =button_equal).grid(row="6", column="1", columnspan="2")
button_clear = Button(root, text="Clear", padx="79", pady="15", command=button_clear).grid(row="4", column="1", columnspan="2")

button_subtract = Button(root, text="-", padx="40", pady="15", command =button_subtract).grid(row="5", column="0")
button_multiply = Button(root, text="x", padx="40", pady="15", command =button_multiply).grid(row="5", column="1")
button_divide = Button(root, text="÷", padx="39", pady="15", command =button_divide).grid(row="5", column="2")

root.mainloop()