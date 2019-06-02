from tkinter import *
import random
import time


root = Tk()
root.geometry("1600x800+0+0")
root.title("HIT Canteen Tickets")


# ---------------------------------------------------------Restaurant info 1 ------------------------------------------------------------------------------------------------
rand = StringVar()
sadza_beans = StringVar()
sadza_beef = StringVar()
rice_beef = StringVar()
rice_chicken = StringVar()
sadza_chicken =  StringVar()
rice_soup =  StringVar()
delta =StringVar()
fizzy = StringVar()
Cost =  StringVar()
Service = StringVar()
Tax =  StringVar()
Subtotal = StringVar()
Total = StringVar()

#-----------------------------------------------------------------------------------------

text_Input = StringVar()
operator = ' '

Tops = Frame(root, width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
# ===============Time================================
localtime = time.asctime(time.localtime(time.time()))
# =========================info=======================
lblinfo = Label(Tops, font=("arial", 44, 'bold'), text="HIT Canteen Tickets", fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=("arial", 20, 'bold'), text=localtime, fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=1, column=0)


# =========================Calculator===========================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = " "
    text_Input.set(' ')


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = " "


def Ref():
    x = random.randint(100000, 900000)
    randomRef = str(x)
    rand.set(randomRef)

    Cosadza_beans = float(sadza_beans.get())
    Cosadza_beef = float(sadza_beef.get())
    Corice_beef = float(rice_beef.get())
    Corice_chicken = float(rice_chicken.get())
    Cosadza_chicken = float(sadza_chicken.get())
    Corice_soup = float(rice_soup.get())
    Codelta = float(delta.get())
    Cofizzy = float(fizzy.get())

    Costofsadza_beans = Cosadza_beans * 2
    Costofsadza_beef = Cosadza_beef * 3.5
    Costofrice_beef = Corice_beef * 4
    Costofrice_chicken = Corice_chicken * 4
    Costofsadza_chicken = Cosadza_chicken * 3.5
    Costofrice_soup = Corice_soup * 1.5
    Costofdelta = Codelta * 4.25
    Costoffizzy = Cofizzy * 1.5

    CostofMeal = ("rtgs", str("%.2f" % (Costofsadza_beans + Costofsadza_beef + Costofrice_beef +
                                       Costofrice_chicken + Costofsadza_chicken  + Costofrice_soup +
                                       Costofdelta + Costoffizzy)))

    PayTax = (Costofsadza_beans + Costofsadza_beef + Costofrice_beef +
              Costofrice_chicken + Costofsadza_chicken + Costofrice_soup +
              Costofdelta + Costoffizzy) * 0.15

    TotalCost = (Costofsadza_beans + Costofsadza_beef + Costofrice_beef +
                 Costofrice_chicken + Costofsadza_chicken + Costofrice_soup +
                 Costofdelta + Costoffizzy)

    Ser_charge = (Costofsadza_beans + Costofsadza_beef + Costofrice_beef +
                  Costofrice_chicken + Costofsadza_chicken + Costofrice_soup +
                  Costofdelta + Costoffizzy) / 99

    Service1 = ('rtgs', str('%.2f' % Ser_charge))

    OverallCost = ('rtgs', str('%.2f' % (PayTax + TotalCost + Ser_charge)))
    PaidTax = ('rtgs', str('%.2f' % PayTax))

    Service.set(Service1)
    Tax.set(PaidTax)
    Cost.set(CostofMeal)
    Subtotal.set(CostofMeal)
    Total.set(OverallCost)


def qExit():
    root.destroy()


def Reset():
    rand.set(" ")
    sadza_beans.set(" ")
    sadza_beef.set(" ")
    rice_beef.set(" ")
    rice_chicken.set(" ")
    sadza_chicken.set(" ")
    rice_soup.set(" ")
    delta.set(" ")
    fizzy.set(" ")
    Cost.set(" ")
    Service.set(" ")
    Tax.set(" ")
    Subtotal.set(" ")
    Total.set(" ")


txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=2, column=2)

addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text='+', bg='powder blue', command=lambda: btnClick("+")).grid(row=2, column=3)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=3, column=2)

subtraction = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='-', bg='powder blue', command=lambda: btnClick("-")).grid(row=3, column=3)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text='*', bg='powder blue', command=lambda: btnClick("*")).grid(row=4, column=3)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                  text='C', bg='powder blue', command=btnClearDisplay).grid(row=5, column=1)

btnEquals = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                   text='=', bg='powder blue', command=btnEqualsInput).grid(row=5, column=2)

Division = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text='/', bg='powder blue', command=lambda: btnClick('/')).grid(row=5, column=3)
#========================================================================================================

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                     bg='powder blue', justify='right')
txtReference.grid(row=0, column=1)

lblsadza_beef = Label(f1, font=('arial', 16, 'bold'), text="Sadza beef", bd=16, anchor="w")
lblsadza_beef.grid(row=1, column=0)
txtsadza_beef = Entry(f1, font=('arial', 16, 'bold'), textvariable=sadza_beef, bd=10, insertwidth=4,
                      bg='powder blue', justify='right')
txtsadza_beef.grid(row=1, column=1)

lblrice_beef = Label(f1, font=('arial', 16, 'bold'), text="Rice beef", bd=16, anchor="w")
lblrice_beef.grid(row=2, column=0)
txtrice_beef = Entry(f1, font=('arial', 16, 'bold'), textvariable=rice_beef, bd=10, insertwidth=4,
                     bg='powder blue', justify='right')
txtrice_beef.grid(row=2, column=1)

lblrice_chicken = Label(f1, font=('arial', 16, 'bold'), text="Rice chicken", bd=16, anchor="w")
lblrice_chicken.grid(row=3, column=0)
txtrice_chicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=rice_chicken, bd=10, insertwidth=4,
                        bg='powder blue', justify='right')
txtrice_chicken.grid(row=3, column=1)

lblsadza_chicken = Label(f1, font=('arial', 16, 'bold'), text="Sadza chicken", bd=16, anchor="w")
lblsadza_chicken.grid(row=4, column=0)
txtsadza_chicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=sadza_chicken, bd=10, insertwidth=4,
                         bg='powder blue', justify='right')
txtsadza_chicken.grid(row=4, column=1)

lblsadza_beans = Label(f1, font=('arial', 16, 'bold'), text="Sadza beans", bd=16, anchor="w")
lblsadza_beans.grid(row=5, column=0)
txtsadza_beans = Entry(f1, font=('arial', 16, 'bold'), textvariable=sadza_beans, bd=10, insertwidth=4,
                       bg='powder blue', justify='right')
txtsadza_beans.grid(row=5, column=1)



lblrice_soup = Label(f1, font=('arial', 16, 'bold'), text="Rice soup", bd=16, anchor="w")
lblrice_soup.grid(row=6, column=0)
txtrice_soup = Entry(f1, font=('arial', 16, 'bold'), textvariable=rice_soup, bd=10, insertwidth=4,
                     bg='powder blue', justify='right')
txtrice_soup.grid(row=6, column=1)

# ---------------------------------------------------------Restaurant info 2 ------------------------------------------------------------------------------------------------
lbldelta = Label(f1, font=('arial', 16, 'bold'), text="Delta cans", bd=16, anchor="w")
lbldelta.grid(row=0, column=2)
txtdelta = Entry(f1, font=('arial', 16, 'bold'), textvariable=delta, bd=10, insertwidth=4,
                 bg='powder blue', justify='right')
txtdelta.grid(row=0, column=3)

lblfizzy = Label(f1, font=('arial', 16, 'bold'), text="Fizzy drinks", bd=16, anchor="w")
lblfizzy.grid(row=1, column=2)
txtfizzy = Entry(f1, font=('arial', 16, 'bold'), textvariable=fizzy, bd=10, insertwidth=4,
                 bg='powder blue', justify='right')
txtfizzy.grid(row=1, column=3)

lblcost = Label(f1, font=('arial', 16, 'bold'), text="Cost", bd=16, anchor="w")
lblcost.grid(row=2, column=2)
txtcost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4,
                bg='#ffffff', justify='right')
txtcost.grid(row=2, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service charge", bd=16, anchor="w")
lblService.grid(row=3, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service, bd=10, insertwidth=4,
                   bg='#ffffff', justify='right')
txtService.grid(row=3, column=3)

lblTax = Label(f1, font=('arial', 16, 'bold'), text="Tax", bd=16, anchor="w")
lblTax.grid(row=4, column=2)
txtTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
               bg='#ffffff', justify='right')
txtTax.grid(row=4, column=3)

lblSubtotal = Label(f1, font=('arial', 16, 'bold'), text="Sub-total", bd=16, anchor="w")
lblSubtotal.grid(row=5, column=2)
txtSubtotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Subtotal, bd=10, insertwidth=4,
                    bg='#ffffff', justify='right')
txtSubtotal.grid(row=5, column=3)

lblTotal = Label(f1, font=('arial', 16, 'bold'), text="Total", bd=16, anchor="w")
lblTotal.grid(row=6, column=2)
txtTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                 bg='#ffffff', justify='right')
txtTotal.grid(row=6, column=3)

# ====================Buttons============================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                  text="Total", bg="powder blue", command=Ref).grid(row=8, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg="powder blue", command=Reset).grid(row=8, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                 text="Exit", bg="powder blue", command=qExit).grid(row=8, column=3)

root.mainloop()
