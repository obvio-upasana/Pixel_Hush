from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
from stegano import lsb
import os

#Set up the Main Window!
root=Tk()
root.title("Pixel Hush - Send me a Pic!")
root.geometry("750x550+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename= filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a Image to Work on", filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lal.configure(image=img,width=250,height=250)
    lal.image=img

def Hide():
    Message=text.get(1.0,END)
    secret=lsb.hide(str(filename),Message)
    secret.save("secret.png")
    


#Title
Label(root,text="Hush", background="#2f4155", foreground="white",font="arial 25 bold underline").place(x=30,y=20)


#Left Side
f= Frame(root, bd=3, bg="black", width=350, height=370 ,relief=GROOVE)
f.place(x=20,y=80)
lal=Label(f,bg="blue")
lal.place(x=40,y=20)


#Right Side
f1= Frame(root, bd=3, bg="white", width=350, height=370,relief=GROOVE)
f1.place(x=400,y=80)
    #for the text input that is to be hideen in the image
text1=Text(f1,font="Roboto 22", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=300)
scrollbar=Scrollbar(f1)
scrollbar.place(x=320, y=0, height=300)
scrollbar.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar.set)

root.mainloop()
