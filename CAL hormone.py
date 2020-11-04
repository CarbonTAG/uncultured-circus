from tkinter import *
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Concentration calculator")

#========================Frames===============================================================
Tops = Frame(root, width=1400, height=20, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=700, height=900, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=600, height=900 ,relief=SUNKEN)
f2.pack(side=RIGHT)

# ===============Time================================
localtime = time.asctime(time.localtime(time.time()))

#===========================Topframe==========================================
lblinfo = Label(Tops, font=("arial", 44, 'bold'), text="Phytohormone concentration calculator", fg="olivedrab4", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=("arial", 20, 'bold'), text=localtime, fg="olivedrab4", bd=16, anchor='w')
lblinfo.grid(row=1, column=0)




#===================Functions=========================================
def Ref():
    aVolume = float(Volume.get())
    aHormone1 = float(Hormone1.get())
    aHormone2 = float(Hormone2.get())
    aHormone3 = float(Hormone3.get())
    aStockHormone1 = float(StockHormone1.get())
    aStockHormone2 = float(StockHormone2.get())
    aStockHormone3 = float(StockHormone3.get())

    x1 = (((aHormone1*1000)/aStockHormone1)*(aVolume/1000))
    x2 = (((aHormone2 * 1000) / aStockHormone2) * (aVolume / 1000))
    x3 = (((aHormone3 * 1000) / aStockHormone3) * (aVolume / 1000))

    a1 = str('%.2f' % x1)
    a2 = str('%.2f' % x2)
    a3 = str('%.2f' % x3)

    HormoneVolume1.set(a1)
    HormoneVolume2.set(a2)
    HormoneVolume3.set(a3)

def qExit():
    root.destroy()


def Reset():
    Volume.set(' ')
    Hormone1.set(' ')
    Hormone2.set(' ')
    Hormone3.set(' ')
    StockHormone1.set(' ')
    StockHormone2.set(' ')
    StockHormone3.set(' ')
#==================Variables========================================


Volume= StringVar()
Hormone1 = StringVar()
Hormone2 = StringVar()
Hormone3 = StringVar()
StockHormone1 = StringVar()
StockHormone2 = StringVar()
StockHormone3 = StringVar()
HormoneVolume1 = StringVar()
HormoneVolume2 = StringVar()
HormoneVolume3 = StringVar()
#============================================================================================
lblVolume = Label(f1, font = ('arial',18, 'bold'), text = 'Volume to be made in ml', fg = "olivedrab4", bd=10,anchor = 'w')
lblVolume.grid(row=1, column=0)
txtVolume = Entry(f1, font=("arial",18, 'bold'), textvariable = Volume, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtVolume.grid(row = 1, column = 1)

lblHormone1 = Label(f1, font =('arial', 18, "bold"), text = 'Hormone1 mg/l', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblHormone1.grid(row=2, column = 0)
txtHormone1= Entry(f1, font=("arial",18, 'bold'), textvariable = Hormone1, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtHormone1.grid(row =2, column = 1)

lblHormone2 = Label(f1, font =('arial', 18, "bold"), text = 'Hormone2 mg/l', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblHormone2.grid(row=3, column = 0)
txtHormone2= Entry(f1, font=("arial",18, 'bold'), textvariable = Hormone2, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtHormone2.grid(row =3, column = 1)

lblHormone3 = Label(f1, font =('arial', 18, "bold"), text = 'Hormone3 mg/l', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblHormone3.grid(row=4, column = 0)
txtHormone3= Entry(f1, font=("arial",18, 'bold'), textvariable = Hormone3, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtHormone3.grid(row =4, column = 1)

lblStockHormone1 = Label(f1, font =('arial', 18, "bold"), text = 'StockHormone1 mg/ml', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblStockHormone1.grid(row=5, column = 0)
txtStockHormone1= Entry(f1, font=("arial",18, 'bold'), textvariable =StockHormone1, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtStockHormone1.grid(row =5, column = 1)

lblStockHormone2 = Label(f1, font =('arial', 18, "bold"), text = 'StockHormone2 mg/ml', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblStockHormone2.grid(row=6, column = 0)
txtStockHormone2= Entry(f1, font=("arial",18, 'bold'), textvariable =StockHormone2, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtStockHormone2.grid(row =6, column = 1)

lblStockHormone3 = Label(f1, font =('arial', 18, "bold"), text = 'StockHormone3 mg/ml', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblStockHormone3.grid(row=7, column = 0)
txtStockHormone3= Entry(f1, font=("arial",18, 'bold'), textvariable =StockHormone3, bd = 10, insertwidth = 4,
                  bg = "olivedrab3", justify = 'right')
txtStockHormone3.grid(row =7, column = 1)


lblHormoneVolume1 = Label(f2, font =('arial', 18, "bold"), text = 'Hormone1 Volume microlitres', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblHormoneVolume1.grid(row=2, column = 3)
txtHormoneVolume1= Entry(f2, font=("arial",18, 'bold'), textvariable = HormoneVolume1, bd = 10, insertwidth = 4,
                  bg = "#ffffff", justify = 'right')
txtHormoneVolume1.grid(row =2, column = 4)

lblHormoneVolume2 = Label(f2, font =('arial', 18, "bold"), text = 'Hormone2 Volume microlitres', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblHormoneVolume2.grid(row=3, column = 3)
txtHormoneVolume2= Entry(f2, font=("arial",18, 'bold'), textvariable = HormoneVolume2, bd = 10, insertwidth = 4,
                  bg = "#ffffff", justify = 'right')
txtHormoneVolume2.grid(row =3, column = 4)

lblHormoneVolume3 = Label(f2, font =('arial', 18, "bold"), text = 'Hormone3 Volume microlitres', bd = 16, fg = 'olivedrab4', anchor = 'w')
lblHormoneVolume3.grid(row=4, column = 3)
txtHormoneVolume3= Entry(f2, font=("arial",18, 'bold'), textvariable =HormoneVolume3, bd = 10, insertwidth = 4,
                  bg = "#ffffff", justify = 'right')
txtHormoneVolume3.grid(row =4, column = 4)

#================Buttons================================================

btnTotal = Button(f2, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                  text="Calculate", bg= "olivedrab3", command=Ref).grid(row=5, column=3)

btnReset = Button(f2, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg= "olivedrab3", command=Reset).grid(row=6, column=3)

btnExit = Button(f2, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                 text="Exit", bg= "olivedrab3", command=qExit).grid(row=7, column=3)

root.mainloop()
