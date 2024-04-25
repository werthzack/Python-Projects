import random
import os

from words import words_with_hints as words #Imports the list of words

def game_start():
    #Initializing variables
    lives = 5
    chosen_word = random.choice(list(words.keys()))
    
    display = []
    for i in chosen_word: 
        display.append("_")
    
    rem_words = len(chosen_word)
    # print(f"Psst the word is {chosen_word}") [For testing purposes]
    
    guessed_letters = []  #To prevent the user from guessing the same letter twice

    # Loops until the player runs out of lives or guesses the word correctly
    while lives > 0:
        guess = input("Guess a Letter ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(guess) > 1:
            print("You can only guess one letter at a time")
        elif not guess.isalpha():
            print("You can only guess letters")
        elif guess in guessed_letters: #Firstly checks if the user has already guessed the letter
            print(f"You've already guessed {guess}")
        else:
            guessed_letters.append(guess)

            if guess in chosen_word: #Then C
                for i in range(len(chosen_word)):
                    letter = chosen_word[i]
                    if letter == guess:
                        display[i] = letter
                        rem_words -= 1

                if rem_words < 1:
                    print("Yay!! You guessed the word")
                    print(f"The word is {chosen_word}")
                    return
            else:
                print(f"Your guess '{guess}' isn't in the word...")
                lives -= 1
        print(' '.join(display))
        print(f"Lives = {lives}")

        if lives < 1:
            print("Oh no! You ran out of lives!!")
            print(f"The word is {chosen_word}")
            return
        elif lives < 3:
            print(f"Hint: {words[chosen_word]}")

game_start()