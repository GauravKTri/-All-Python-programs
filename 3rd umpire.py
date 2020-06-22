import tkinter
import cv2 #pip inatall opencv-python
import PIL.Image, PIL.ImageTK #pip install pillow
import threading
from functools import partial
import time
import imutils

stream=cv2.VideoCapture("clip.mp4")

def play(speed):
    print(f"you clicked on play.speed is {speed}")
   
        #play the vedio in reverse mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMS)
    stream.set(cv2.CAP_PROP_POS_FRAMS,frame1+speed)
        
    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    framePIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    canvas.creat_text(120,25,fill="green",font="times 20 italic bold",text="Decision Pending")

def pending(decison):
    # display decision pending image
    frame=cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray())
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #wait for 1 second
    time.sleep(1)
    #display sponsor image
    frame=cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray())
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #wait for 1.5 second
    time.sleep(1.5)
    #display out/notout image
    if decision=='out':
        decisionImg="out.png"
    else:
        decisionImg="not_out.png"


    frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray())
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #wait for 1.5 second
    

def out():
    thread =threading.Thred(target=pending,args=("out",))
    thread.daemon=1
    thread.start()       
    print("player is out")


def not_out():
    thread =threading.Thred(target=pending,args=("not out",))
    thread.daemon=1
    thread.start() 
    print("player is not out")


#width and hieght of our main screen

SET_WIDTH= 650
SET_HEIGHT=368
#Tkinter gui starts here
window=tkinter.tk()
window.title("third umpire decision")
cv_img=cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas= tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)

photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.creat_image(0,0,ancho=tkinter.NM,image=photo)
canvas.pack()

#buttons to control playback
btn=tkinter.Button(window,text="<< previous (fast)",width=50,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<< previous (slow)",width=50,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text=" Next(slow)>>",width=50,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text=" Next(fast)>>",width=50,command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text=" Give Out",width=50,command=out)
btn.pack()

btn=tkinter.Button(window,text=" Give Not Out",width=50,command=not_out)
btn.pack()
window.mainloop()
