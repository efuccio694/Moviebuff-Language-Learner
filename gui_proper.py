#import main

from tkinter import *

root = Tk()
root.geometry('400x500') #sets the window size

selection_label = Label(root, text = 'Select an operating mode.')
selection_label.grid(row=0, column=1)

realtime_translator_button = Button(root, text = 'Realtime Translator')
flashcard_creator_button = Button(root, text= 'Flashcard Creator')
play_flashcards_button = Button(root, text = 'Play Flashcards')

realtime_translator_button.grid(row=1, column=0, padx=10)
flashcard_creator_button.grid(row=1, column=1)
play_flashcards_button.grid(row=1, column=2, padx=10)


root.mainloop()
