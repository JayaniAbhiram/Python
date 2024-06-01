# my_tkinter_app.py
import tkinter 
from tkinter import *
window = Tk()
window.minsize(width=500,height=400)

label = Label(text="i am a label",font=("times new roman", 30))
label.pack()

def buttonClick():
    print("the button is clicked")
    inputValue = input.get()
    # print(inputValue)
    label.config(text=inputValue)


button = Button(text = "click me", command=buttonClick)
button.pack()

input = Entry(width=15)
input.pack()




window.mainloop()