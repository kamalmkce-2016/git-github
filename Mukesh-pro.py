from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x1000+0+0")
root.title("PYTO MAPS")

text_Input = StringVar()
operator=""


Tops = Frame(root, width = 1600,height= 50, bg = "powder blue", relief = RAISED)
Tops.pack(side = TOP)

f1 = Frame(root, width = 750, height= 700,relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 350,height= 700, bg = "powder blue", relief = SUNKEN)
f2.pack(side = RIGHT,padx=5)
#===================================Time======================================
localtime = time.asctime(time.localtime(time.time()))
#===================================Info======================================
lblinfo = Label(Tops,font = ('arial',50,'bold'),text="PYTHON RESTAURENT SYSTEM",fg = "steel blue",bd = 10,anchor = 'w')
lblinfo.grid(row=0,column=0)

lblinfo = Label(Tops,font = ('arial',20,'bold'),text=localtime,fg = "steel blue",bd = 10,anchor = 'w')
lblinfo.grid(row=1,column=0)
#===================================Calculator======================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup =  str(eval(operator))
    text_Input.set(sumup)
    operator = ""
def Ref():
    x = random.randint(1000,99999)
    Refnuum = str(x)
    rand.set(Refnuum)

    CoF = float(Fries.get())
    CoB = float(Burger.get())
    CoFl = float(Filet.get())
    CoD = float(Drinks.get())
    CoCb = float(Chicken_Burger.get())
    CoCh = float(Cheese_Burger.get())

    CostofFries = CoF * 110
    CostofBurger = CoB * 10
    CostofFillet = CoF * 20
    CostofDrinks = CoD * 5
    Costofcb = CoCb * 15
    Costofch = CoCh * 40

    CostofMeal = ("Rs",str('%.2f'%(CostofFries + CostofBurger + CostofFillet + CostofDrinks +  Costofcb + Costofch)))

    PayTax =((CostofFries + CostofBurger + CostofFillet + CostofDrinks + Costofcb + Costofch) * 0.17)

    Totalcost =(CostofFries + CostofBurger + CostofFillet + CostofDrinks +  Costofcb + Costofch)

    ser_charge = ((CostofFries + CostofBurger + CostofFillet + CostofDrinks +  Costofcb + Costofch)/99)

    Service_ch = "Rs.",str('%.2f'%ser_charge)

    overallcost = "Rs.",str('%.2f'%(PayTax + Totalcost + ser_charge))

    paidtax = "Rs.",str('%.2f'%(PayTax))

    Service.set(Service_ch)
    Cost.set(CostofMeal)
    Tax.set(paidtax)            
    SubTotal.set(CostofMeal)
    Total.set(overallcost)
    
def qexit():
    root.destroy()
def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")          
    

txtdisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtdisplay.grid(columnspan=4)

bt7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='7',bg="powder blue",command = lambda: btnClick(7)).grid(row=2,column=0)
bt8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='8',bg="powder blue",command = lambda: btnClick(8)).grid(row=2,column=1)
bt9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='9',bg="powder blue",command = lambda: btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='+',bg="powder blue",command = lambda: btnClick("+")).grid(row=2,column=3)
#------------------------------------------------------------------------------------------------------------
bt4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='4',bg="powder blue",command = lambda: btnClick(4)).grid(row=3,column=0)
bt5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='5',bg="powder blue",command = lambda: btnClick(5)).grid(row=3,column=1)
bt6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='6',bg="powder blue",command = lambda: btnClick(6)).grid(row=3,column=2)
Subraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='-',bg="powder blue",command = lambda: btnClick('-')).grid(row=3,column=3)
#------------------------------------------------------------------------------------------------------------
bt1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='1',bg="powder blue",command = lambda: btnClick(1)).grid(row=4,column=0)
bt2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='2',bg="powder blue",command = lambda: btnClick(2)).grid(row=4,column=1)
bt3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='3',bg="powder blue",command = lambda: btnClick(3)).grid(row=4,column=2)
Multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='*',bg="powder blue",command = lambda: btnClick('*')).grid(row=4,column=3)
#-------------------------------------------------------------------------------------------------------------
bt0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='0',bg="powder blue",command = lambda: btnClick(0)).grid(row=5,column=0)
btClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='C',bg="powder blue",command = lambda: btnClearDisplay()) .grid(row=5,column=1)
btEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='=',bg="powder blue",command = lambda: btnEquals()).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
           text='/',bg="powder blue",command = lambda: btnClick('/')).grid(row=5,column=3)
#-------------------------------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()
#1----------------------------------------------------------------------------------------------------------------------
lb1reference = Label(f1,font=('arial',16,'bold'),text="reference",bd =16, anchor='w')
lb1reference.grid(row=0,column =0)
txtreference = Entry(f1,font=('arial',16,'bold'),text=rand,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtreference.grid(row=0,column =1)
#2----------------------------------------------------------------------------------------------------------------------
lb1fries = Label(f1,font=('arial',16,'bold'),text="ChickenBiriyani",bd =16, anchor='w')
lb1fries.grid(row=1,column =0)
txtfries = Entry(f1,font=('arial',16,'bold'),text=Fries,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtfries.grid(row=1,column =1)
#3----------------------------------------------------------------------------------------------------------------------
lb1Burger = Label(f1,font=('arial',16,'bold'),text="Kalaki",bd =16, anchor='w')
lb1Burger.grid(row=2,column =0)
txtBurger = Entry(f1,font=('arial',16,'bold'),text=Burger,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtBurger.grid(row=2,column =1)
#4----------------------------------------------------------------------------------------------------------------------
lb1Filet = Label(f1,font=('arial',16,'bold'),text="Dosa",bd =16, anchor='w')
lb1Filet.grid(row=3,column =0)
txtFilet = Entry(f1,font=('arial',16,'bold'),text=Filet,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtFilet.grid(row=3,column =1)
#--8--------------------------------------------------------------------------------------------------------------------
lblDrinks = Label(f1,font=('arial',16,'bold'),text="idly",bd =16, anchor='w')
lblDrinks.grid(row=4,column =0)
txtDrinks = Entry(f1,font=('arial',16,'bold'),text=Drinks,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtDrinks.grid(row=4,column =1)
#------11----------------------------------------------------------------------------------------------------------------
lblChicken_Burger = Label(f1,font=('arial',16,'bold'),text="Parota",bd =16, anchor='w')
lblChicken_Burger.grid(row=5,column =0)
txtChicken_Burger = Entry(f1,font=('arial',16,'bold'),text=Chicken_Burger,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtChicken_Burger.grid(row=5,column =1)
#--------12--------------------------------------------------------------------------------------------------------------
lblCheese_Burger = Label(f1,font=('arial',16,'bold'),text="Pongal",bd =16, anchor='w')
lblCheese_Burger.grid(row=0,column =3)
txtCheese_Burger = Entry(f1,font=('arial',16,'bold'),text=Cheese_Burger,bd =10, insertwidth =4,bg="powder blue", justify ='right')
txtCheese_Burger.grid(row=0,column =4)

#################################################################
#----10------------------------------------------------------------------------------------------------------------------
lblcost = Label(f1,font=('arial',16,'bold'),text="cost",bd =16, anchor='w')
lblcost.grid(row=1,column =3)
txtcost = Entry(f1,font=('arial',16,'bold'),text=Cost,bd =10, insertwidth =4,bg="#ffffff", justify ='right')
txtcost.grid(row=1,column =4)
#-7---------------------------------------------------------------------------------------------------------------------
lblservice = Label(f1,font=('arial',16,'bold'),text="Service",bd =16, anchor='w')
lblservice.grid(row=2,column =3)
txtservice = Entry(f1,font=('arial',16,'bold'),text=Service,bd =10, insertwidth =4,bg="#ffffff", justify ='right')
txtservice.grid(row=2,column =4)

#---9-------------------------------------------------------------------------------------------------------------------
lbltax = Label(f1,font=('arial',16,'bold'),text="Tax",bd =16, anchor='w')
lbltax.grid(row=3,column =3)
txttax = Entry(f1,font=('arial',16,'bold'),text=Tax,bd =10, insertwidth =4,bg="#ffffff", justify ='right')
txttax.grid(row=3,column =4)

#5----------------------------------------------------------------------------------------------------------------------
lb1sub = Label(f1,font=('arial',16,'bold'),text="SubTotal",bd =16, anchor='w')
lb1sub.grid(row=4,column =3)
txtsub = Entry(f1,font=('arial',16,'bold'),text=SubTotal,bd =10, insertwidth =4,bg="#ffffff", justify ='right')
txtsub.grid(row=4,column =4)
#6----------------------------------------------------------------------------------------------------------------------
lbltotal = Label(f1,font=('arial',16,'bold'),text="Total",bd =16, anchor='w')
lbltotal.grid(row=5,column =3)
txttotal = Entry(f1,font=('arial',16,'bold'),text=Total,bd =10, insertwidth =4,bg="#ffffff", justify ='right')
txttotal.grid(row=5,column =4)

#------------------------------------------------------      BUTTONS   ----------------------------------------------------------------

btnTotal = Button(f1,padx = 16,pady = 8,bd =16,fg="black",font=('arial',16,'bold'),width =10,text="Total", bg="powder blue",command = Ref).grid(row = 7,column =4)
btnqexit = Button(f1,padx = 16,pady = 8,bd =16,fg="black",font=('arial',16,'bold'),width =10,text="Exit", bg="powder blue",command = qexit).grid(row = 8,column =1)
btnReset = Button(f1,padx = 16,pady = 8,bd =16,fg="black",font=('arial',16,'bold'),width =10,text="Reset", bg="powder blue",command = Reset).grid(row = 7,column =1)



root.mainloop()


