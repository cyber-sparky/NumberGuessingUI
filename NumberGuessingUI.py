from glob import glob
from tkinter import *

root =Tk()
root.geometry('500x500')
root.title("Number Guessing Game")

#=------------------------------------------------------------------------------------------------------------------------------------

middle=50
counter=8

text = StringVar()
text.set("Is the number you think greater than %d?" %middle)
disp_text=Label(root,textvariable=text).pack()
entry_window = Entry(root,width=40,borderwidth=4).pack()

def Okay(value):
    global counter
    global middle
    if value == "yes" or 'y' or 'N':
        if (counter==7):
            middle=middle+25
            return middle
        elif (counter==6):
            middle=middle+12
            return middle
        elif (counter==5):
            middle=middle+6
            return middle
        elif (counter==4):
            middle=middle+3
            return middle
        elif (counter==3):
            middle=middle+2
            return middle
        elif (counter==2):
            middle=middle+1
            return middle
        elif (counter==1):
            counter=0
            middle=middle+1
            return middle 
    elif value=='n' or value=='N' or value=="no":
        if (counter==7):
            middle=middle-25
            return middle
        elif (counter==6):
            middle=middle-12
            return middle
        elif (counter==5):
            middle=middle-6
            return middle
        elif (counter==4):
            middle=middle-3
            return middle
        elif (counter==3):
            middle=middle-2
            return middle
        elif (counter==2):
            middle=middle-1
            return middle
        elif (counter==1):
            counter=0
            return middle             
while (counter!=0):
    text.set("Is the number you think greater than %d?" %middle)   
    value = entry_window.__getattribute__            
    middle=Okay(value)
btn_okay = Button(root, text="Okay",command=Okay)


root.mainloop()