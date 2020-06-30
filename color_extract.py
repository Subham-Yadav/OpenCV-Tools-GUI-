from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2

low = list()
up = list()
def get_values():
    global low,up
    l = lower.get("1.0","end-1c")
    u = upper.get("1.0","end-1c")
    l = list(l.split(' '))
    u = list(u.split(' '))
    for i in range(3):
        low.append(int(l[i]))
        up.append(int(u[i]))


def fileDialog():
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype=(("JPG file","*.jpeg"),("all files","*.*")))
    if filename != None:
        img = cv2.imread(filename)
        lower = np.array(low)
        upper = np.array(up)
        blur = cv2.GaussianBlur(img, (7,7), 0)
        blurred = cv2.blur(blur, (9,9))
        mask = cv2.inRange(blurred, lower, upper)
        res = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow('res', res)


def Webcam():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame,1)
        lower = np.array(low)
        upper = np.array(up)
        blur = cv2.GaussianBlur(frame, (7,7), 0)
        blurred = cv2.blur(blur, (9,9))
        mask = cv2.inRange(blurred, lower, upper)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('res', res)
        k = cv2.waitKey(5) & 0xFF
        if k==27:
            break

    cv2.destroyAllWindows()
    cap.release()
        

new_win = Tk()
new_win.title('OpecnCV Tools')
new_win.geometry("450x200")

lower=Text(new_win, height=1, width=10)
lower.grid(row=1, column=1, padx=30, pady=(20,0))
l = Label(new_win, text="Lower value(B G R)")
l.config(font=("Courier", 8))
l.grid(row=2, column=1, padx=20)

upper=Text(new_win, height=1, width=10)
upper.grid(row=1, column=3, padx=30, pady=(20,0))
u = Label(new_win, text="Upper value(B G R)")
u.config(font=("Courier", 8))
u.grid(row=2, column=3, padx=20)

ok = Button(new_win, text = "OK", command = get_values)
ok.grid(row=3, column=2, padx=30, pady=(20,0))

open_file = Button(new_win, text = "Image",command = fileDialog)
open_file.grid(row=4, column=1, padx=30, pady=(20,0))

apply_button = Button(new_win, text="Webcam", command=Webcam)
apply_button.grid(row=4, column=3, padx=20, pady=(20,0))

new_win.mainloop()
