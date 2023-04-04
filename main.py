import tkinter
from tkinter import *

# main window
calc = Tk()
calc.geometry('300x355')
calc.resizable(False, False)

# frames
f_result = tkinter.Frame(calc, width=300, height=35)
f_result.pack_propagate(0)
f_op1 = tkinter.Frame(calc, width=70, height=200)
f_op1.grid_propagate(0)
f_op2 = tkinter.Frame(calc, width=70, height=200)
f_op2.grid_propagate(0)
f_buttons = tkinter.Frame(calc, width=150, height=200)

# Var
# used to indicate the operation the calc will do
op = 0
# used to remind the number before the operation button is called
bfnumber = ''


# Functions

# sets the label value when the user press a new number or call a operation
def setlabelvalue(value, isresult=False):
    global lb_master
    if isresult is True or lb_master['text'] == str(0) and value != '.':
        lb_master['text'] = str(value)
    else:
        lb_master['text'] = lb_master['text'] + str(value)


# calculate and update label value
def result(value, operation):
    global lb_master
    global bfnumber
    if operation == 1:
        setlabelvalue(int(bfnumber) + int(value), True)
    elif operation == 2:
        setlabelvalue(int(bfnumber) - int(value), True)
    elif operation == 3:
        setlabelvalue(int(bfnumber) / int(value), True)
    elif operation == 4:
        setlabelvalue(int(bfnumber) * int(value), True)
    else:
        unexpectederror = Tk()
        unexpectederror.title('Erro')
        unexpectederror.geometry('200x100')
        errbtn = Button(unexpectederror, text='Ok', command=unexpectederror.destroy)

        errbtn.pack()


# everytime a operation is called, this function sets globally
# the number that represents the operation in a variable
# and same way sets globally the before number that changed
# this is called everytime a operation is called
def setopbfn(operation, bfn):
    global op
    global bfnumber
    global lb_master
    lb_master['text'] = str(0)
    op = operation
    bfnumber = bfn


# Objetcs
lb_master = Label(f_result, text='0',
                  font='Arial 15')
btn1 = Button(f_buttons, text='1', command=lambda: setlabelvalue(1), width=6, height=2)
btn2 = Button(f_buttons, text='2', command=lambda: setlabelvalue(2), width=6, height=2)
btn3 = Button(f_buttons, text='3', command=lambda: setlabelvalue(3), width=6, height=2)
btn4 = Button(f_buttons, text='4', command=lambda: setlabelvalue(4), width=6, height=2)
btn5 = Button(f_buttons, text='5', command=lambda: setlabelvalue(5), width=6, height=2)
btn6 = Button(f_buttons, text='6', command=lambda: setlabelvalue(6), width=6, height=2)
btn7 = Button(f_buttons, text='7', command=lambda: setlabelvalue(7), width=6, height=2)
btn8 = Button(f_buttons, text='8', command=lambda: setlabelvalue(8), width=6, height=2)
btn9 = Button(f_buttons, text='9', command=lambda: setlabelvalue(9), width=6, height=2)
btn0 = Button(f_buttons, text='0', command=lambda: setlabelvalue(0), width=6, height=2)
btn_add = Button(f_op1, text='+', width=9, height=2, command=lambda: setopbfn(1, lb_master['text']))
btn_dim = Button(f_op1, text='-', width=9, height=2, command=lambda: setopbfn(2, lb_master['text']))
btn_div = Button(f_op2, text='/', width=9, height=2, command=lambda: setopbfn(3, lb_master['text']))
btn_mult = Button(f_op2, text='*', width=9, height=2, command=lambda: setopbfn(4, lb_master['text']))
btn_pnt = Button(f_op2, text='.', width=9, height=2, command=lambda: setlabelvalue('.'))
btn_rs = Button(f_op1, text='=', width=9, height=2, command=lambda: result(lb_master['text'], op))


# gridding & packing
f_result.pack(side='top')
f_op1.pack(side='left', anchor='nw')
f_buttons.pack(side='left', anchor='nw')
f_op2.pack(side='left', anchor='nw')
lb_master.pack()
btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=0, row=2)
btn5.grid(column=1, row=2)
btn6.grid(column=2, row=2)
btn7.grid(column=0, row=3)
btn8.grid(column=1, row=3)
btn9.grid(column=2, row=3)
btn0.grid(column=1, row=4)
btn_add.grid(column=0, row=1)
btn_dim.grid(column=0, row=2)
btn_rs.grid(column=0, row=3)
btn_div.grid(column=0, row=1)
btn_mult.grid(column=0, row=2)
btn_pnt.grid(column=0, row=3)

calc.mainloop()
