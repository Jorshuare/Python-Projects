from tkinter import *


def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)


def clear():
    global operator
    operator = ""
    txt_input.set("")
    # Display.insert(0, "Start Calculating...")


def equal():
    global operator
    sumup = eval(operator)
    txt_input.set(sumup)
    operator = ""


win = Tk()
win.title("Calculator")
win.resizable(False, False)

operator = ""
txt_input = StringVar(value="Start Calculating...")

# Screen
Display = Entry(win, font=("Arial", 30, "bold"), fg="white", bg="green",
                bd=50, justify="right", textvariable=txt_input)  # note the bd
Display.grid(columnspan=4)  # columnspan means occupy four columns

# =======================Row1=========================
btn7 = Button(win, padx=30, pady=15, text="7", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(7))
btn7.grid(row=1, column=0)

btn8 = Button(win, padx=30, pady=15, text="8", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(8))
btn8.grid(row=1, column=1)

btn9 = Button(win, padx=30, pady=15, text="9", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(9))
btn9.grid(row=1, column=2)

btnC = Button(win, padx=30, pady=15, text="C", bg="Green", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=clear)
btnC.grid(row=1, column=3)

# =======================Row1=========================
btn4 = Button(win, padx=30, pady=15, text="4", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(4))
btn4.grid(row=2, column=0)

btn5 = Button(win, padx=30, pady=15, text="5", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(5))
btn5.grid(row=2, column=1)

btn6 = Button(win, padx=30, pady=15, text="6", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(6))
btn6.grid(row=2, column=2)

btnplus = Button(win, padx=33, pady=15, text="+", bg="Orange", fg="black",
             font=("Arial", 30, "bold"), bd=8, command=lambda:btn("+"))
btnplus.grid(row=2, column=3)

# =======================Row1=========================
btn1 = Button(win, padx=30, pady=15, text="1", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(1))
btn1.grid(row=3, column=0)

btn2 = Button(win, padx=30, pady=15, text="2", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(2))
btn2.grid(row=3, column=1)

btn3 = Button(win, padx=30, pady=15, text="3", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda: btn(3))
btn3.grid(row=3, column=2)

btnx = Button(win, padx=38, pady=15, text="-", bg="Orange", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda:btn("-"))
btnx.grid(row=3, column=3)

# =======================Row1=========================
btn0 = Button(win, padx=30, pady=15, text="0", bg="White", fg="black",
              font=("Arial", 30, "bold"), bd=8, command=lambda:btn("0"))
btn0.grid(row=4, column=0)

btn_dot = Button(win, padx=30, pady=15, text=" .", bg="Orange", fg="black",
                 font=("Arial", 30, "bold"), bd=8, command=lambda:btn("."))
btn_dot.grid(row=4, column=1)

btn_div = Button(win, padx=30, pady=15, text=" /", bg="Orange", fg="black",
                 font=("Arial", 30, "bold"), bd=8, command=lambda:btn("/"))
btn_div.grid(row=4, column=2)

btn_mul = Button(win, padx=33, pady=15, text="x", bg="Orange", fg="black",
                 font=("Arial", 30, "bold"), bd=8, command=lambda:btn("*"))
btn_mul.grid(row=4, column=3)

# =======================Row1=========================
btn_equ = Button(win, padx=95, pady=15, text="=", bg="Green", fg="black",
                 font=("Arial", 30, "bold"), bd=8, command=equal)
btn_equ.grid(row=5, column=0, columnspan=2)

btn_bra1 = Button(win, padx=30, pady=15, text=" (", bg="Orange", fg="black",
                  font=("Arial", 30, "bold"), bd=8, command=lambda:btn("("))
btn_bra1.grid(row=5, column=2)

btn_bra2 = Button(win, padx=30, pady=15, text=" )", bg="Orange", fg="black",
                  font=("Arial", 30, "bold"), bd=8, command=lambda:btn(")"))
btn_bra2.grid(row=5, column=3)

# btn_mul = Button(win,padx=30, pady=15,text="x", bg="Orange", fg="black",
#              font=("Arial", 30,"bold"), bd=8)
# btn_mul.grid(row=5,column=3)


win.mainloop()
