#Moviebuff-Language-Learner
#Authored by Evan Fuccio and Brayden Yan
"""pip install googletrans==3.1.0a0"""
import random
from googletrans import Translator
MAX_CARDS = 500
class Flashcard:
    def __init__(self, card_number, selected_word, translated_selected_word):
        self.card_number = card_number
        self.selected_word = selected_word
        self.translated_selected_word = translated_selected_word
    
    def play_flashcard(self):
        print(f'Word: {self.selected_word}')
        flip = input('Flip? (y/n): ')
        if flip == 'y':
            print(f'Meaning: {self.translated_selected_word}\n')

def main():
    file_name = input("Enter entire script file name with extension: ")
    
    #checks if the input is a valid file name
    file_name = checkfile(file_name)

    run_mode = set_run_mode()
    if run_mode == '1':
        realtime_translator(file_name)
    elif run_mode == '2':
        flashcard_creator(file_name)
    elif run_mode == '3':
        play_flashcards()
    else:
        print('Error: Improper run mode. Restart program and try again.')


    
    # #converts srt file to usable list
    # srt_to_list(file_name)
    # #Finds the subtitles associated with the timestamp
    # text = find_subtitle(srt_to_list(file_name))
    # #translates the subtitle
    # translator(text)

def set_run_mode ():
    print('Select run mode: ')
    print('1: Realtime Translator')
    print('2: Flashcard Creator')
    print('3: Play Flashcards')
    run_mode = input('Mode: ')
    return run_mode

def realtime_translator(file_name):
    srt_to_list(file_name)
    #Finds the subtitles associated with the timestamp
    text = find_subtitle(srt_to_list(file_name))
    #translates the subtitle
    translated_text = translator(text)
    print(translated_text)

def flashcard_creator(file_name):
    srt_to_list(file_name) #converts srt to list

    times_of_run = int(input("How many flashcards would you like to make?"))
    
    for i in range(0,times_of_run):

        text = find_subtitle(srt_to_list(file_name))

        print('What word would you like to create a flashcard from?')
        
        foreign_words = text.split() #splits the text into a list of words

        index = 0 #prints out different words as options
        for word in foreign_words:
            print(f'{index}: {word}')
            index+=1
        
        selected_word = foreign_words[int(input())] #gets the selected_word from user
        translated_selected_word = translator(selected_word) #translates selected_word
        #print(translated_selected_word)
        card_number = random.randint(0, MAX_CARDS)
        card_number = Flashcard(card_number, selected_word, translated_selected_word )
        flashcard_file = open('Flashcards.txt', 'a')
        flashcard_file.write(f'{card_number.card_number} {card_number.selected_word} {card_number.translated_selected_word} \n')
        flashcard_file.close()

def play_flashcards():
    try:
        #open flashcard_file
        flashcard_file = open(r'Flashcards.txt', 'r')
        flashcard_lines = flashcard_file.readlines()
        for line in flashcard_lines:
            card_info = line.split()
            card_number = card_info[0]

            card_number = Flashcard(card_info[0], card_info[1], card_info[2]) #creates an object for each line

            card_number.play_flashcard()
        flashcard_file.close() #closes flashcard file 
    except:
        print('Error: No flashcards have been created. Restart program and make flashcards before trying to play them.')
    
    

def checkfile(name):

    isfile = False
    while isfile == False:
        try:
            test = open(name)
            isfile = True
            test.close()
            return name
        except:
            name = input("Try again, enter entire script file name with extension: ")



def translator (text):

    sub_translator = Translator()
    translated_text = sub_translator.translate(text)
    
    return(translated_text.text)
    #print(translated_text.text)



def srt_to_list (srt):

    line_list = []

    open_file = open(srt, "r", encoding = r'utf8') #opens our srt file in read mode

    #writes each line of the file into a location in the 
    for line in open_file: 
        line_list.append(line) 
    
    open_file.close()

    #cleanups line_list
    #current_index=0

    for current_index in range(0, len(line_list)):
    #removes all instances of newline
    #if line_list[current_index] == '\n':
    #line_list.remove(line_list[current_index])
    #current_index -=1
        
        #removes newline from text files
        if line_list[current_index] != '\n':
            line_list[current_index] = line_list[current_index].replace('\n', '')
            
    #loop through list, if timestamp, append the two timestamps
    final_list = []
    count = 0
    subtitle = ''
    for line in line_list:
        #if the line is a timestamp, append the two timestamps to the final_list
        if len(line) > 4 and line[:1].isnumeric() and line[2] == ':':
            split_timestamp_line = line.split()
            #Gets both timestamps in one line, formats them ignoring milliseconds, and appends them to final_list
            first_timestamp = split_timestamp_line[0][:8]
            first_timestamp = int(first_timestamp.replace(':',''))
            final_list.append(first_timestamp)
            
            second_timestamp = split_timestamp_line[2][:8]
            second_timestamp = int(second_timestamp.replace(':',''))
            final_list.append(second_timestamp)

       
        if line_list[count][1:2].isalpha():
            subtitle = subtitle + ' ' + line_list[count]
            #subtitle = subtitle.replace(f"\","")

        if count < (len(line_list)-1):
            if line_list[count+1] == '\n':
                final_list.append(subtitle) 
                subtitle = '' #resets the subtitle variable
        count +=1

    return final_list



def find_subtitle(final_list):
    user_time = input("Input the current timestamp in this format: Hours:Minutes:Seconds \nExample: 01:04:45 ")
    user_time = int(user_time.replace(':', ''))

    index = 0
    for values in final_list:
        if isinstance(values, int) and isinstance(final_list[index+1], int):
            if index != (len(final_list) - 1) and index != len(final_list) and user_time >= final_list[index] and user_time <= final_list[index+1]:
                print(final_list[index+2])
                return final_list[index+2] #the associated subtitle

        index +=1

main()