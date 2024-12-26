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
    Message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),Message)
    secret.save("secret.png")
    
def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def Save():
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save as")
    if filename:
        os.replace("secret.png", filename + ".png")

#UI Elements

#Title
Label(root,text="Hush", background="#2f4155", foreground="white",font="arial 25 bold underline").place(x=30,y=20)


#Left Side
f1= Frame(root, bd=3, bg="black", width=350, height=370 ,relief=GROOVE)
f1.place(x=20,y=80)
lal=Label(f1,bg="blue")
lal.place(x=40,y=20)


#Right Side
f2= Frame(root, bd=3, bg="white", width=350, height=370,relief=GROOVE)
f2.place(x=400,y=80)
    #for the text input that is to be hideen in the image
text1=Text(f2,font="Roboto 22", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=300)
scrollbar=Scrollbar(f2)
scrollbar.place(x=320, y=0, height=300)
scrollbar.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar.set)

#Left Bottom
f3=Frame(root,bd=3,bg='#2f4155', width=335, height=95, relief=GROOVE)
f3.place(x=20, y=450)
    #Buttons for open and save an image
Button(f3, text="OPEN", width=10, height=2, font="arial 14",command=showimage).place(x=25,y=24)
Button(f3, text="SAVE", width=10, height=2, font="arial 14",command=Save).place(x=200,y=24)
Label(f3, text="Picture, Image, Photo File", bg='#2f4155', fg="yellow").place(x=5,y=1)

#Right Bottom
f4=Frame(root,bd=3,bg='#2f4155', width=335, height=95, relief=GROOVE)
f4.place(x=400,y=450)
    #Buttons
Button(f4, text="HIDE", width=10, height=2, font="arial 14 bold",command=Hide).place(x=25,y=24)
Button(f4,text="SHOW",width=10, height=2, font="arial 14 bold",command=Show).place(x=200,y=24)
Label(f4, text="Picture, Image, Photo File", bg='#2f4155', fg="yellow").place(x=5,y=1)

root.mainloop()
