#imports everything from tkinter
from tkinter import *

root = Tk()

#create a function for what the button should do
def myClick():
    myLabel = Label(root, text='Look! I clicked a button!')
    myLabel.pack()

myButton = Button(root, text="Click Me!", command = myClick, bg='blue', fg='white')
myButton.pack()




root.mainloop()