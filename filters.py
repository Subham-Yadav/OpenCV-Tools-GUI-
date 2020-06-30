from __future__ import print_function
from tkinter import *
from tkinter import filedialog
import cv2


filter_name = ""
file = ""
def ok():
    global filter_name
    filter_name = var.get()

def fileDialog():
    global file
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype=(("JPG file","*.jpeg"),("all files","*.*")))
    if filename != None:
        file = filename

def apply():
    if file!=None:
        img = cv2.imread(file, 0)
        if filter_name=="BONE":
            image = cv2.applyColorMap(img, cv2.COLORMAP_BONE)
        elif filter_name=="WINTER":
            image = cv2.applyColorMap(img, cv2.COLORMAP_WINTER)
        elif filter_name=="OCEAN":
            image = cv2.applyColorMap(img, cv2.COLORMAP_OCEAN)
        elif filter_name=="HOT":
            image = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
        else:
            image = cv2.applyColorMap(img, cv2.COLORMAP_PINK)
        cv2.imshow("{0} filter applied".format(filter_name), image)

new_win = Tk()
new_win.title('Filters')
new_win.geometry("300x150")

var = StringVar(new_win)
var.set("BONE")

option = OptionMenu(new_win, var, "BONE", "WINTER", "OCEAN", "HOT", "PINK")
option.grid(row=1, column=1, padx=30, pady=(20,0))

option_button = Button(new_win, text="Confirm", command=ok)
option_button.grid(row=1, column=2, padx=30, pady=(20,0))

open_file = Button(new_win, text = "Browse A File",command = fileDialog)
open_file.grid(row=2, column=1, padx=30, pady=(20,0))

apply_button = Button(new_win, text="Apply", command=apply)
apply_button.grid(row=2, column=2, padx=20, pady=(20,0))

new_win.mainloop()
