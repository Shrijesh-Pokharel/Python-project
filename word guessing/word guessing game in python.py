##word guessing game in python
import random

words= ['kindly', 'recite', 'repeat', 'tree', 'display', 'geeks', 'coader', 'programmer', 'python', 'premium', 'watch']

print(words)

word =random.choice(words)

print("Welcome to Word Guessing Game")

space = ['_']* len(word)

def get_letter_position(guess, word, space):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character= '*'
            word = word[:index]+removed_character+word[index +  1:]
            space[index] = guess
        else:
            index= -1
    return (word, space)

def win_check():
    for i in range(0, len(space)):
        if  space[i] == '_':
            return -1
    return 1

num_turns= len(word)
for i in range(-1, num_turns):
    guess= input("guess the character :")

    if guess in word:
        word,space = get_letter_position(guess, word, space)
        print(space)
    else:
        print('sorry! wrong letter')
    
    if win_check( )== 1 :
        print('congratulation you won!!!!!')
        break

    print('you have '+str(num_turns - i -1)+' turns left.')
    print()