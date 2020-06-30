import os
import cv2
from tkinter import *
from tkinter import filedialog
import numpy as np
from matplotlib import pyplot as plt

def fileDialog():
    global file, var
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype=(("JPG file","*.jpeg"),("all files","*.*")))
    if filename != None:
        file = filename
        image = cv2.imread(file)
        var.set(str(image.shape[0])+", "+str(image.shape[1])+", "+str(image.shape[2]))

def plot_histogram(image, title, mask):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("No. of pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0,256])
        plt.plot(hist, color=color)
        plt.xlim([0,256])
    plt.show()


def apply():
    if file!=None:
        img = cv2.imread(file)
        mask = np.zeros(img.shape[:2], dtype='uint8')
        plot_histogram(img, 'histogram', mask=None)

new_win = Tk()
new_win.title('Plot Histogram')
new_win.geometry("340x150")

open_file = Button(new_win, text = "Browse A File",command = fileDialog)
open_file.grid(row=1, column=1, padx=(30,0), pady=(20,0))

var = StringVar()
img_dim = Label(new_win, textvariable = var, text="Image Dimensions")
img_dim.grid(row=1, column=3, padx=0, pady=(20,0))
#Text
w = Label(new_win, text="Image Dimensions")
w.config(font=("Courier", 8))
w.grid(row=2, column=3, padx=0)

apply_button = Button(new_win, text="Apply", command=apply)
apply_button.grid(row=3, column=2, padx=20, pady=(20,0))

new_win.mainloop()
