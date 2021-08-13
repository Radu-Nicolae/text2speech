#importing the pyttsx library
import time

import pyttsx3

#initialisation
engine = pyttsx3.init()

#app
def getFinalString():
    print("Welcome! Enter down below a text that you want to be converted to speech")
    user_input = input("Your answer: ")
    char_array = list(user_input)
    word = ''
    newString = ''
    i = 0

    while i < len(char_array):
        if char_array[i] == ' ':
            engine.say(word)
            char_array[i] = ' '
            word = ''

        word += char_array[i]
        i += 1
        if i == len(char_array):
            engine.say(word)

    return newString

getFinalString()
engine.runAndWait()

