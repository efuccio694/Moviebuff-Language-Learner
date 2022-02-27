# The Moviebuff Language Learner
### Learn new languages through the power of film! Pause at any moment within a film and translate the spoken words live and create flashcards to practice the language and expand your vocabulary!
## Inspiration
This project was inspired by my great grandmother who, after immigrating to Pittsburgh from Germany, learned English through watching movies at her local movie theater. While at the time, this was the only way to view movies, technology has now allowed us to view films at home. I wanted to create a program that would make learning new languages through film, as my great grandmother did, easier, and allow for people to practice foreign languages and expand their knowledge through viewing films and creating associated flashcards.
## How to install
To install first you will need to install the google translate api. To install type in the command
`pip install googletrans==3.1.0a0`

Then you will need to clone the repository using
`git clone https://github.com/efuccio694/Moviebuff-Language-Learner`
## Requirements
The user will have to source the .srt subtitle file for the film in the original language. We recommend https://www.opensubtitles.org/en/search/subs to find one!
The user must rename their .srt file to a .txt file in order for the program to function
```Example: Amelie.srt -------> Amelie.txt ```
## What it does
### Live Translate
#### Did not catch that line?
After providing a source srt file, the user will be able to pause the movie, and enter the timestamp in order to translate that line of dialogue into English.

### Flashcard Creator
#### Make flashcards to practice new vocabulary from the film!
After providing a source srt file, the user will be able to pause the movie, and enter the timestamp. The program will prompt the user for which word in the subtitle they want to create a flashcard for and will create a translated flashcard written in the Flashcards.txt file.

*Flashcards will be written to Flashcards.txt in this format:*
Flashcard Number | Original Text | Translated to English Text

### Play Flashcards
#### Practice through all the flashcards you created through the terminal.
If you have created flashcards using the Flashcard Creator mode, the program will run through them in order for you to practice. Type `y` to flip each flashcard.

## How we built it

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for Moviebuff Language Learner
The next thing we would like to add to our program in the future would be a GUI so that Moviebuff Language Learner will be easier to use and more visually appealing. We would also like the program to automate the renaming of the .srt file to a .txt file so that the user will not have to prepare their .srt file in that way before running the program. 
