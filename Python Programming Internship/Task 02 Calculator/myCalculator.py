from tkinter import *

#Created Function to update entry on every click
def updateEntry(value):
    myMainLabel.insert("end",value)

#Created Function to delete entry on Clear Button Click
def removeEntry():
    myMainLabel.delete(0,"end")

#Created Function to calculate values entered in entry
def calculateEntry():
    expression = myMainLabel.get()
    result = str(eval(expression))
    myMainLabel.delete(0,"end")
    myMainLabel.insert(0,result)

root = Tk()

#Set title of my software
root.title(" My Calculator ")

#set the width and height of my software
root.geometry("350x430")

#Set icon of my calculator
myIcon = PhotoImage(file="icon2.png")
root.iconphoto(False,myIcon)

# Main Display Screen
myMainLabel = Entry(root,text="",width=14,borderwidth=3,font=('Times New Roman',35,"bold"),justify="right",bg="#8c8c8c")
myMainLabel.grid(pady=15,row=0,column=0,padx=5,columnspan=7)

# Disabling Maximize Button 
root.resizable(width=False, height=False)

#Set window color
root.configure(bg="#000000")


# Creating Buttons
buttonNumber3 = Button(root,text="+",width=7,height=4,bg="#f0ad4e",command=lambda:updateEntry("+"))
buttonNumber3.grid(row=1,column=0)


buttonNumber4 = Button(root,text="/",width=7,height=4,bg="#f0ad4e",command=lambda:updateEntry("/"))
buttonNumber4.grid(row=3,column=0)

buttonNumber5 = Button(root,text="*",width=7,height=4,bg="#f0ad4e",command=lambda:updateEntry("*"))
buttonNumber5.grid(row=5,column=0)

buttonNumber6 = Button(root,text="-",width=7,height=4,bg="#f0ad4e",command=lambda:updateEntry("-"))
buttonNumber6.grid(row=7,column=0)

buttonNumber7 = Button(root,text="7",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("7"))
buttonNumber7.grid(row=1,column=1)

buttonNumber8 = Button(root,text="8",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("8"))
buttonNumber8.grid(row=1,column=2)

buttonNumber9 = Button(root,text="9",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("9"))
buttonNumber9.grid(row=1,column=3)


buttonNumber10 = Button(root,text="4",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("4"))
buttonNumber10.grid(row=3,column=1)

buttonNumber11 = Button(root,text="5",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("5"))
buttonNumber11.grid(row=3,column=2)

buttonNumber12 = Button(root,text="6",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("6"))
buttonNumber12.grid(row=3,column=3)


buttonNumber13 = Button(root,text="1",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("1"))
buttonNumber13.grid(row=5,column=1)

buttonNumber14 = Button(root,text="2",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("2"))
buttonNumber14.grid(row=5,column=2)

buttonNumber15 = Button(root,text="3",width=7,height=4,bg="#d4d4d2",fg = "black",command=lambda:updateEntry("3"))
buttonNumber15.grid(row=5,column=3)

buttonNumber16 = Button(root,text="C",width=7,height=4,bg="#f0ad4e",fg = "black",command=removeEntry)
buttonNumber16.grid(row=7,column=1)

buttonNumber17 = Button(root,text="%",width=7,height=4,bg="#f0ad4e",fg = "black",command=lambda:updateEntry("%"))
buttonNumber17.grid(row=7,column=2)

buttonNumber18 = Button(root,text="=",width=7,height=4,bg="#f0ad4e",fg = "black",command=calculateEntry)
buttonNumber18.grid(row=7,column=3)


root.mainloop()