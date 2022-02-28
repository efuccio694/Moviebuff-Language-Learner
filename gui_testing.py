#imports everything from tkinter
from tkinter import *

#in tkinter, everything is a widget
#the first thing we create is the root widget (a window)

#creates an instance of the Tk object that is our root widget
root = Tk()

#Creates a Label widget (text)
myLabel = Label(root, text = "Hello World!")
#shoving Label widget onto the screen
myLabel.pack()

#EVENT LOOP
#loops to figure out what is going on on the GUI
root.mainloop()