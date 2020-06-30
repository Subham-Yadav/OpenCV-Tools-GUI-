from tkinter import *
import os

##Functions
def funcOne():
    exec(open("gradient.py").read(), globals())

def funcTwo():
    exec(open("histogram.py").read(), globals())

def funcThree():
    exec(open("filters.py").read(), globals())

def funcFour():
    exec(open("color_extract.py").read(), globals())

###Window
root = Tk()
root.title('OpecnCV Tools')
root.geometry("650x600")

##Button 1
b1 = Button(root, command = funcOne, justify = LEFT)
photo_1 = PhotoImage(file = "Images/threshold.png")
b1.config(image = photo_1, width="250", height="200")
b1.pack(side=LEFT)
b1.grid(row=1, column= 1, padx=30, pady=(40,0))
#Button1 Text
w1 = Label(root, text="Gradient Detection")
w1.config(font=("Courier", 18))
w1.grid(row=2, column= 1, padx=30)

##Button 2
b2 = Button(root, command = funcTwo)
photo_2 = PhotoImage(file="Images/histogram.png")
b2.config(image=photo_2, width="250", height="200")
b2.grid(row=1, column=2, padx=30, pady=(40,0))
#Button2 Text
w2 = Label(root, text="Histogram")
w2.config(font=("Courier", 18))
w2.grid(row=2, column=2, padx=30)

##Button 3
b3 = Button(root, command = funcThree)
photo_3 = PhotoImage(file ="Images/filter.png")
b3.config(image=photo_3, width="250", height="200")
b3.grid(row=3, column=1, padx=30, pady=(40,0))
#Button3 Text
w3 = Label(root, text="Filters")
w3.config(font=("Courier", 18))
w3.grid(row=4, column=1, padx=30)

##Button 4
b4 = Button(root, command = funcFour)
photo_4 = PhotoImage(file="Images/color_filter.png")
b4.config(image=photo_4, width="250", height="200")
b4.grid(row=3, column=2, padx=30, pady=(40,0))
#Button4 Text
w4 = Label(root, text="Color Extraction")
w4.config(font=("Courier", 18))
w4.grid(row=4, column=2, padx=30)

root.iconbitmap("Images/icon.ico")
root.resizable(0, 0)
root.mainloop()
