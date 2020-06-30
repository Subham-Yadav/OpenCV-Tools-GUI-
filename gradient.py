from tkinter import *
from tkinter import filedialog
import cv2


gradient_name = ""
file = ""
def ok():
    global gradient_name
    gradient_name = var.get()

def fileDialog():
    global file
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype=(("JPG file","*.jpeg"),("all files","*.*")))
    if filename != None:
        file = filename

def use_threshold():
    image = cv2.imread(file, 0)
    ret,thresh = cv2.threshold(image,60,255,cv2.THRESH_BINARY)
    cv2.imshow("Simple threshold", thresh)

def use_adapativeThreshold():
    image = cv2.imread(file, 0)
    bilateral = cv2.bilateralFilter(image, 15, 25, 25)
    thresh = cv2.adaptiveThreshold(bilateral,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imshow("Adaptive Gaussian Threshold", thresh)

def use_otsu():
    image = cv2.imread(file, 0)
    blur = cv2.GaussianBlur(image,(7,7),0)
    #bilateral = cv2.bilateralFilter(image, 15, 25, 25)
    blur = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow("Otsu after Gaussian Filtering", thresh)

def apply():
    if file!=None:
        if gradient_name=="threshold":
            use_threshold()
        if gradient_name=="adapativeThreshold":
            use_adapativeThreshold()
        if gradient_name=="otsu":
            use_otsu()

new_win = Tk()
new_win.title('OpecnCV Tools')
new_win.geometry("300x150")

var = StringVar(new_win)
var.set("threshold")

option = OptionMenu(new_win, var, "threshold", "adapativeThreshold", "otsu")
option.grid(row=1, column=1, padx=30, pady=(20,0))

option_button = Button(new_win, text="Confirm", command=ok)
option_button.grid(row=1, column=2, padx=30, pady=(20,0))

open_file = Button(new_win, text = "Browse A File",command = fileDialog)
open_file.grid(row=2, column=1, padx=30, pady=(20,0))

apply_button = Button(new_win, text="Apply", command=apply)
apply_button.grid(row=2, column=2, padx=20, pady=(20,0))

new_win.mainloop()
