import tkinter as tk
import tkinter.font as tkFont
from main import *

class App:
    def __init__(self, root):
        #setting title
        root.title("Moviebuff Language Learner")
        #setting window size
        width=400
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_4=tk.Label(root)
        ft = tkFont.Font(family='Ariel',size=14)
        GLabel_4["font"] = ft
        GLabel_4["fg"] = "#333333"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "Select an operating mode"
        GLabel_4.place(x=80,y=30,width=245,height=30)

        RT_Button=tk.Button(root)
        RT_Button["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Ariel',size=10)
        RT_Button["font"] = ft
        RT_Button["fg"] = "#000000"
        RT_Button["justify"] = "center"
        RT_Button["text"] = "Realtime Translator"
        RT_Button.place(x=80,y=80,width=242,height=51)
        RT_Button["command"] = self.RT_Button_command
        
        FCC_Button=tk.Button(root)
        FCC_Button["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Ariel',size=10)
        FCC_Button["font"] = ft
        FCC_Button["fg"] = "#000000"
        FCC_Button["justify"] = "center"
        FCC_Button["text"] = "Flashcard Creator"
        FCC_Button.place(x=80,y=140,width=242,height=51)
        FCC_Button["command"] = self.FCC_Button_command


        PF_Button=tk.Button(root)
        PF_Button["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Ariel',size=10)
        PF_Button["font"] = ft
        PF_Button["fg"] = "#000000"
        PF_Button["justify"] = "center"
        PF_Button["text"] = "Play Flashcards"
        PF_Button.place(x=80,y=200,width=242,height=51)
        PF_Button["command"] = self.PF_Button_command

    def FCC_Button_command(self):
        super_translator(2)


    def RT_Button_command(self):
        super_translator(1)


    def PF_Button_command(self):
        super_translator(3)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
