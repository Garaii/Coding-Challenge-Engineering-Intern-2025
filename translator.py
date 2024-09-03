import sys


# Hi, I'm Ikram Gara, here is my approach to the Engeneering Inter Coding Challenge for Winter 2025


# creating a sort of hashmap for the letters, numbers and special character to translate to braille and vice-versa
char_2_braille = {"a":"o.....", "b":"o.o...", "c":"oo....", "d":"oo.o..", "e":"o..o..", "f":"ooo...", "g":"oooo..", "h":"o.oo..", "i":".oo...", "j":".ooo..", "k":"o...o.", "l":"o.o.o.", "m":"oo..o.","n":"oo.oo.","o":"o..oo.","p":"ooo.o.","q":"ooooo.","r":"o.ooo.","s":".oo.o.","t":".oooo.","u":"o...oo","v":"o.o.oo","w":".ooo.o","x":"oo..oo","y":"oo.ooo","z":"o..ooo", " ":"......", ".":"..oo.o",",":"..o...","?":"..o.oo","!":"..ooo.",":":"..oo..",";":"..o.o.","-":"....oo","/":".o..o.","(":"o.o..o",")":".o.oo."}
braille_decim = {".":"..oo.o",",":"..o...","?":"..o.oo","!":"..ooo.",":":"..oo..",";":"..o.o.","-":"....oo","/":".o..o.","<":".oo..o",">":"o..oo.","(":"o.o..o",")":".o.oo."," ":"......"}
braille_num = {"1":"o.....", "2":"o.o...", "3":"oo....", "4":"oo.o..", "5":"o..o..", "6":"ooo...", "7":"oooo..", "8":"o.oo..", "9":".oo...", "0":".ooo.."}

#Creating the opposite hashmap of the letters and the braille code so we will be able to translate one from the other
braille_2_char = {v: k for k, v in char_2_braille.items()}  
braille_2_num = {v : k for k, v in braille_num.items()}

#creating a Hash Map for the type of character we will be encountering
type_braille = {"number": ".o.ooo", "capital": ".....o", "decimal": ".o...o"}

# this function will verify if the following function is made of letters or braille code
def braille_verificator(str):
    length_check = len(str) % 6 == 0
    character_check = all(char == 'o' or char =='.' for char in str)
    return length_check and character_check

# THIS FUNCTION WILL TRANSLATE ENGLISH TO BRAILLE
def translator_2_braille(message_braille):
    length_string = len(message_braille)
    final = []   #the string willl be stored in this list

    #to make sure we will not be repeating the type of character braille we will need to create a switch that we will turn on and off accordingly
    number_mode = False    
    letter_mode = False

    #looping through the string to trasform each char to its braille code
    for char in message_braille:
       
        if char.isalpha():   # verifying if the char is a letter

            if char.isupper(): #if the braille is an UpperCase
                if not letter_mode:
                    final.append(type_braille["capital"]) #adding the braille code accordingly
                    letter_mode= True # turning on the switch so the braille code will not be added multiple times in the code
                final.append(char_2_braille[char.lower()])
            else:
                final.append(char_2_braille[char.lower()]) 
        elif char.isdigit(): # verifying if the char is a number
            if not number_mode: #if the braille code for digits is not added we will add it
                final.append(type_braille["number"])
                number_mode = True
            final.append(braille_num[char])
        else: 
            final.append(char_2_braille.get(char, "")) 
    return ''.join(final) #joining the list into a string

#this function transfor braille into english letters
def translator_2_english(string_braille):
    
    # creating the variable that will store the text that is translated into a list of characters
    final = []
    i=0
    length = len(string_braille)

    #looping through the braille string 
    while i < length:
        type = string_braille[i:i+6] #making sure we catch every letter since braille in of length 6
        
        if type == type_braille["capital"]: #if the braille is Uppercase we will translate accordingly
            i += 6
            next_char = string_braille[i:i+6]
            final.append(braille_2_char[next_char].upper())
        elif type == "......": #making sure we dont go over the spaces in the translation
            final.append(" ")
        elif type == type_braille["number"]: #translating the numbers to get from the right hashmap
            i += 6
            next_char = string_braille[i:i+6]
            final.append(braille_2_num[next_char])
        else:
            final.append(braille_2_char[type]) 
        i += 6
            
    return ''.join(final) #joining the list into a string


def main():
    #making sure we have enough arguments on the command line to translate
    if len(sys.argv) < 2:
        print("Error: Two arguments needed for usage") #Error catching if arguments missing
        return
    encoded = ' '.join(sys.argv[1:]) #joining them into one string to make it easier
    
    #if braille is detected we send the string into the right function
    if braille_verificator(encoded): 
       print(translator_2_english(encoded))
    else: 
        print(translator_2_braille(encoded))
        
if __name__ == "__main__":
    main()