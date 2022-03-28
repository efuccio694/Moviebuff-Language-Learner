#imports everything from tkinter
from tkinter import *

root = Tk()
root.geometry('400x500')
e = Entry(root, width=50)
e.pack()
#create a function for what the button should do
def myClick():
    myLabel = Label(root, text='Look! I clicked a button!', font=('Ariel',12))
    myLabel.pack()

myButton = Button(root, text="Click Me!", command = myClick, bg='blue', fg='white')
myButton.pack()




root.mainloop()