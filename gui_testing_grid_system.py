#imports everything from tkinter
from tkinter import *

#in tkinter, everything is a widget
#the first thing we create is the root widget (a window)

#creates an instance of the Tk object that is our root widget
root = Tk()

#Creates a Label widget (text)
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My name is Evan Fuccio")

# #shoving Label widget onto the screen
# myLabel1.pack()

#using grid system to place the labels
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

#EVENT LOOP
#loops to figure out what is going on on the GUI
root.mainloop()