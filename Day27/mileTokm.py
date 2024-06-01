from tkinter import *

window = Tk()
window.minsize(height=500,width=500)


label = Label(text="mile to km converter")
label.grid(column=2,row=2)

labelMile = Label(text="Enter the value in miles")
labelMile.grid(column=2,row=3)
inputmile = Entry()
inputmile.grid(column=2,row=4)



def toKm():
    inputMileValue = float(inputmile.get())
    change = inputMileValue * 2

    labelKm.config(text = change)




labelkmm = Label(text="is equal to")
labelkmm.grid(column=1,row=2)

labelKm = Label(text="0")
labelKm.grid(column=3,row=3)




convertbtn = Button(text="convert",command=toKm)
convertbtn.grid(column=2,row=5)







window.mainloop()