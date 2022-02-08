from tkinter import *
import random

window = Tk()

window.minsize(500,500)
window.maxsize(600,600)

window.title('Roll Dice Simulator')

label = Label(window,font=('bold',400))
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()

heading = Label(window,text='Roll Dice Simulator',font=('bold',30),bg='red')
heading.pack(fill=X)

button = Button(window,text='Roll',font=('normal',20),command=lambda:roll())
button.pack()


window.mainloop()