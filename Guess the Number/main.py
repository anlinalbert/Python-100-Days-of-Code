import random
from art import logo

# Print logo
print(logo)

# Assign random number
randomNumber = random.randint(1, 100)
retryCount = 0

def checkGuess(guess):
    """Check whether the guess was correct or not."""
    if guess < randomNumber:
        return "low"
    elif guess > randomNumber:
        return "high"
    else:
        return "correct"
    
def setDifficultyLevel(difficulty):
    """Set the difficulty level of the game."""
    global retryCount
    if difficulty == 'hard':
        retryCount = 5
    else:
        retryCount = 10

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

setDifficultyLevel(input("Choose a difficulty. Type 'easy' or 'hard': "))
    
while(retryCount >= 1):
    print(f"You have {retryCount} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    ifCorrectGuess = checkGuess(guess)

    if ifCorrectGuess == "correct":
        print(f"You got it! The answer was {guess}.")
        break
    elif ifCorrectGuess == "low":
        print("Too low.")
    elif ifCorrectGuess == "high":
        print("Too high.")
    retryCount -= 1
    
    if retryCount >= 1:
        print("Guess again.")
        
if retryCount == 0:
    print("You've run out of guesses, you lose.")