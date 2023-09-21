from tkinter import*
import math

# Creating window
root = Tk()
root.geometry("490x400")
root.resizable(False, False)
root.title("Calculator")
root.config(bg="sky blue")

a = StringVar()

# Entry Box
ent = Entry(root, font=("calibre",  20),  fg='white', justify="right", relief="raised",bg="grey", textvariable=a)
ent.place(x=5, y=10, width=470, height=50)

# Functions:
def show(op):
    a.set(a.get()+op)

def eq(y):
    exp = a.get()
    y=eval(exp)
    a.set(y)

def clear():
    a.set("")

def fact():
    if a.get() == "":
        a.set("Error")
    else:
        exp = int(a.get())

        factorial = math.factorial(exp)
        a.set(factorial)
def sqrt():
    if a.get() == "":
        a.set("Error")
    else:
        exp = int(a.get())

        sqrt1 = math.sqrt(exp)
        a.set(sqrt1)

# Creating buttons
can1 = Button(root, text='C', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=clear)
can1.place(x=375, y=70, width=90, height=50)

sqrt1 = Button(root, text='√', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=sqrt)
sqrt1.place(x=5, y=70, width=90, height=50)

pie = Button(root, text='π', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
pie.place(x=125, y=70, width=90, height=50)
pie.configure(command=lambda: show("3.14159265359"))

exp = Button(root, text='e', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=lambda: show("2.71828182846"))
exp.place(x=250, y=70, width=90, height=50)

# Creating Number Buttons

b1 = Button(root, text='1', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b1.place(x=5, y=125, width=90, height=50)
b1.configure(command=lambda: show("1"))

b2 = Button(root, text='2', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b2.place(x=125, y=125, width=90, height=50)
b2.configure(command=lambda : show("2"))

b3 = Button(root, text='3', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b3.place(x=250, y=125, width=90, height=50)
b3.configure(command=lambda: show("3"))

b4 = Button(root, text='4', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b4.place(x=5, y=180, width=90, height=50)
b4.configure(command=lambda: show("4"))

b5 = Button(root, text='5', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b5.place(x=125, y=180, width=90, height=50)
b5.configure(command=lambda: show("5"))

b6 = Button(root, text='6', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b6.place(x=250, y=180, width=90, height=50)
b6.configure(command=lambda: show("6"))

b7 = Button(root, text='7', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b7.place(x=5, y=235, width=90, height=50)
b7.configure(command=lambda: show("7"))

b8 = Button(root, text='8', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
b8.place(x=125, y=235, width=90, height=50)
b8.configure(command=lambda: show("8"))



b9 = Button(root, text='9', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=lambda: show("9"))
b9.place(x=250, y=235, width=90, height=50)

zer0 = Button(root, text='0', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=lambda: show("0"))
zer0.place(x=125, y=290, width=90, height=50)

# Arithmetic Buttons

dec = Button(root, text='.', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=lambda: show("."))
dec.place(x=250, y=290, width=90, height=50)

s1 = Button(root, text='-', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
s1.place(x=375, y=180, width=90, height=50)
s1.configure(command=lambda: show("-"))

a1 = Button(root, text='+', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
a1.place(x=375, y=125, width=90, height=50)
a1.configure(command=lambda: show("+"))

mul = Button(root, text='x', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised')
mul.place(x=375, y=235, width=90, height=50)
mul.configure(command=lambda: show("*"))

d1 = Button(root, text='/', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=lambda: show("/"))
d1.place(x=375, y=290, width=90, height=50)

f1 = Button(root, text='!', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=fact)
f1.place(x=5, y=290, width=90, height=50)

beq = Button(root, text='=', font=('Ariel', 20), activebackground="grey", bg='white', fg='black', relief='raised', command=lambda: eq("="))
beq.place(x=5, y=345, width=475, height=50)

root.mainloop()