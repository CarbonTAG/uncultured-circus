from tkinter import *

root = Tk()
root.title("Simple Calculator")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)
    
def button_clear():
    e.delete(0, END)    

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#=============Define Buttons================================
Btn1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda : button_click(1))
Btn2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda : button_click(2))
Btn3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda : button_click(3))
Btn4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda : button_click(4))
Btn5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda : button_click(5))
Btn6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda : button_click(6))
Btn7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda : button_click(7))
Btn8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda : button_click(8))
Btn9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda : button_click(9))
Btn0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda : button_click(0))

Btn_add =  Button(root, text = '+', padx = 40, pady = 20, command = button_add)
Btn_equal =  Button(root, text = '=', padx = 82, pady = 20, command = button_equal)
Btn_clear =  Button(root, text = 'Clear', padx = 80, pady = 20, command = button_clear)

Btn_subtract =  Button(root, text = '-', padx = 40, pady = 20, command = button_subtract)
Btn_multiply =  Button(root, text = 'x', padx = 40, pady = 20, command = button_multiply)
Btn_divide =  Button(root, text = '/', padx = 40, pady = 20, command = button_divide)

# put buttons on the screen

Btn1.grid(row = 3 , column = 0)
Btn2.grid(row = 3, column = 1)
Btn3.grid(row = 3, column =2 )

Btn4.grid(row = 2 , column = 0)
Btn5.grid(row = 2, column = 1)
Btn6.grid(row = 2, column = 2)

Btn7.grid(row = 1, column = 0)
Btn8.grid(row = 1, column = 1)
Btn9.grid(row = 1, column = 2)

Btn0.grid(row = 4 , column = 0 )

Btn_add.grid(row = 5 , column = 0)
Btn_equal.grid(row = 5, column = 1, columnspan = 2)
Btn_clear.grid(row = 4, column = 1, columnspan = 2)

Btn_subtract.grid(row = 6, column = 0)
Btn_multiply.grid(row = 6 , column = 1)
Btn_divide.grid(row = 6, column = 2)


#Btn.grid(row = , column = )








root.mainloop()

