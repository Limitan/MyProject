# coding: cp1251
from random import randint
from tkinter import *

counttrue = 0
countincorrect = 0
def clicked():
    res = int('{}'.format(txt.get()))
    if a + b == res:
        global counttrue
        counttrue += 1
        counting = Label(window, text = ("Верных ответов:" + str(counttrue)), font=("Calibri", 30))
        counting.grid(row=1, column=0)
    else:
        global countincorrect
        countincorrect += 1
        countingincorrect = Label(window, text = ("Неверных ответов:" + str(countincorrect)), font=("Calibri", 30))
        countingincorrect.grid(row=2, column=0)

window = Tk()
window.title('Numbers')
window.geometry('600x250')
lbl = Label(window, text = '', font=("Calibri", 60))
txt = Entry(window, width = 2, font =("Calibri", 60)) 
txt.grid(column=1, row=0)
btn = Button(window, text="Ответить", command=clicked, font =("Calibri", 30))  
btn.grid(column=2, row=0)

while True:
    a = randint(0, 20)
    b = randint(0, 20)
    if a + b <= 20:
        a = a
        b = b
        lbl.configure(text = (str(a), '+', str(b), '='))
        lbl.grid(row=0, column=0)
        counting = Label(window, text = ("Верных ответов:" + str(counttrue)), font=("Calibri", 30))
        counting.grid(row=1, column=0)
        counting = Label(window, text = ("Неверных ответов:" + str(countincorrect)), font=("Calibri", 30))
        counting.grid(row=2, column=0)
        break


window.mainloop()

