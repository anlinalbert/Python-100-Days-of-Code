import random
import hangman_art
import hangman_words

# Priting logo
print(hangman_art.logo)

# Initial variables
end_of_game = False
lives = 6

# Getting a random word from 'word_list'
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")
    
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter is in word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"Letter '{guess}' is not present in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    else:
        print(f"Letter '{guess}' was present in the word.")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])