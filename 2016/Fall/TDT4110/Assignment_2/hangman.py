import os
from sys import platform

secret_word = list(input('\n    Welcome to python-hangman!\n\n    What word should the player find out?: ')) #Read in the secret word
guessed_word= list('*'*len(secret_word))
lives = int(input('    And how many lives do the player have?: '))

########################    Hide the secret word    ########################
def clear():
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')
clear()
########################    /Hide the secret word    #######################


name=input('\n    Hi, and welcome to python-hangman!\n    Please tell me your name: ')
print("\n    Let's start ",name,'! Your word looks like this "',''.join(guessed_word),'". Good luck!\n',sep='')
while secret_word!=guessed_word:
    if lives>0:
        i=0
        guess = input('    Guess a letter: ')

        if guess==str(''.join(secret_word)):
            guessed_word=list(guess)
        elif guess in secret_word:
            while i<len(secret_word):
                if guess==secret_word[i]:
                    guessed_word[i]=guess
                i+=1
        else:
            lives-=1
            if lives > 1:
                print('    Be careful, You have only',lives,'lives left!')
            else:
                print('    Be careful, You have only',lives,'life left!')
        print("    So far you've got:",''.join(guessed_word))
    else:
        clear()
        print('\n\n    You lost the game. :( Sorry. The secred word was: ',''.join(secret_word),'.\n\n        ________\n        | /    |\n        |/     O\n        |     /|\ \n        |     / \ \n        |\n       ------------\n',sep='')
        break
else:
    print('    You won! The secret word was:',''.join(guessed_word),'\n\n        ________\n        | /    \n        |/      \n        |    \O/\n        |     | \n        |    / \ \n       ------------\n')
