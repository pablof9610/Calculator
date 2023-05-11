import tkinter
from tkinter import *

# main window
calc = Tk()
calc.geometry('300x355')
calc.resizable(False, False)

# frames
f_result = tkinter.Frame(calc, width=300, height=35)
# this holds the frame resize to the elements packed on it
f_result.pack_propagate(0)
f_op1 = tkinter.Frame(calc, width=70, height=200)
# do the same thing with the elements gridded on it
f_op1.grid_propagate(0)
f_op2 = tkinter.Frame(calc, width=70, height=200)
f_op2.grid_propagate(0)
f_buttons = tkinter.Frame(calc, width=150, height=200)

# Var

# used to indicate the operation the calc will do
op = 0

# used to reconize when the calc is making operations
# without clicking on "=" and then switch the number
# after a operation is called and concatenate the next ones
acum = False

# used to check if the operation button is called enought times
# to show the result without clicking on the "="
opcounter = 0

# used to remind the number before the operation button is called
bfnumber = ''

# Functions

# sets the label value when the user press a new number or call a operation
def setlabelvalue(value, isresult=False, isc = False):
    global lb_master
    global acum
    global bfnumber
    global opcounter
    if (('.' in lb_master['text']) and (value == '.')):
        pass
    else:
        if ((isresult is True) or ((lb_master['text'] == str(0)) and (value != '.')) or ((opcounter > 1) and (acum is True))):
            lb_master['text'] = str(value)
            if (acum is True):
                acum = False
        else:
            lb_master['text'] = lb_master['text'] + str(value)
    if isc == True:
        bfnumber = 0
        opcounter = 0

def transform_value_type(value):
    if '.' in value:
        return float(value)
    else:
        return int(value)

# calculate and update label value
def result(value, operation, isequal = False):
    global lb_master
    global bfnumber
    value = transform_value_type(value)
    if operation == 1:
        setlabelvalue(bfnumber + value, True)
        return bfnumber + value
    elif operation == 2:
        setlabelvalue(bfnumber - value, True)
        return bfnumber - value
    elif operation == 3:
        setlabelvalue(bfnumber / value, True)
        return bfnumber / value
    elif operation == 4:
        setlabelvalue(bfnumber * value, True)
        return bfnumber * value
    else:
        unexpectederror = Tk()
        unexpectederror.title('Erro')
        unexpectederror.geometry('200x100')
        errbtn = Button(unexpectederror, text='Ok', command=unexpectederror.destroy)
        errbtn.pack()
    if isequal == True:
        opcounter = 0


# everytime a operation is called, this function sets globally
# the number that represents the operation in a variable
# and same way sets globally the before number that changed
def setopbfn(operation, bfn):
    global op
    global bfnumber
    global lb_master
    global opcounter
    global acum
    opcounter += 1
    if opcounter > 1:
        if operation != op:
            bfnumber = result(lb_master['text'], op)
            acum = True
        else:
            bfnumber = result(lb_master['text'], operation)
            acum = True
    else: 
        bfnumber = transform_value_type(bfn)
        lb_master['text'] = str(0)
    op = operation


# Objetcs
lb_master = Label(f_result, text='0', font='Arial 15')
btn1 = Button(f_buttons, text='1', command=lambda: setlabelvalue(1), width=6, height=2).grid(column=0, row=1)
btn2 = Button(f_buttons, text='2', command=lambda: setlabelvalue(2), width=6, height=2).grid(column=1, row=1)
btn3 = Button(f_buttons, text='3', command=lambda: setlabelvalue(3), width=6, height=2).grid(column=2, row=1)
btn4 = Button(f_buttons, text='4', command=lambda: setlabelvalue(4), width=6, height=2).grid(column=0, row=2)
btn5 = Button(f_buttons, text='5', command=lambda: setlabelvalue(5), width=6, height=2).grid(column=1, row=2)
btn6 = Button(f_buttons, text='6', command=lambda: setlabelvalue(6), width=6, height=2).grid(column=2, row=2)
btn7 = Button(f_buttons, text='7', command=lambda: setlabelvalue(7), width=6, height=2).grid(column=0, row=3)
btn8 = Button(f_buttons, text='8', command=lambda: setlabelvalue(8), width=6, height=2).grid(column=1, row=3)
btn9 = Button(f_buttons, text='9', command=lambda: setlabelvalue(9), width=6, height=2).grid(column=2, row=3)
btn0 = Button(f_buttons, text='0', command=lambda: setlabelvalue(0), width=6, height=2).grid(column=1, row=4)
btn_add = Button(f_op1, text='+', width=9, height=2, command=lambda: setopbfn(1, lb_master['text'])).grid(column=0, row=1)
btn_dim = Button(f_op1, text='-', width=9, height=2, command=lambda: setopbfn(2, lb_master['text'])).grid(column=0, row=2)
btn_div = Button(f_op2, text='/', width=9, height=2, command=lambda: setopbfn(3, lb_master['text'])).grid(column=0, row=1)
btn_mult = Button(f_op2, text='*', width=9, height=2, command=lambda: setopbfn(4, lb_master['text'])).grid(column=0, row=2)
btn_pnt = Button(f_op2, text='.', width=9, height=2, command=lambda: setlabelvalue('.')).grid(column=0, row=3)
btn_rs = Button(f_op1, text='=', width=9, height=2, command=lambda: result(lb_master['text'], op)).grid(column=0, row=3)
btn_clear = Button(f_op1, text='C', width=9, height=2, command=lambda: setlabelvalue(0, True, True)).grid(column=0, row=4)


# gridding & packing
f_result.pack(side='top')
f_op1.pack(side='left', anchor='nw')
f_buttons.pack(side='left', anchor='nw')
f_op2.pack(side='left', anchor='nw')
lb_master.pack()

calc.mainloop()