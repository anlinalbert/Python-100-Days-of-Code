import random
import os
from game_data import data
from art import logo, vs

# Initial variables
score = 0
result = False

def printLogo():
    """Clear screen and print logo."""
    os.system("cls")
    print(logo)

def checkAnswer(guess):
    """Used to check if the guessed answer is correct or not."""
    global score
    if guess == "A":
        if personOne["follower_count"] > personTwo["follower_count"]:
            score += 1
        else:
            return True
    else:
        if personTwo["follower_count"] > personOne["follower_count"]:
            score += 1
        else:
            return True

while not result:
    printLogo()
    
    if not result and score != 0:        
        print(f"You're right! Current score: {score}")
        
    personOne = random.choice(data)
    personTwo = random.choice(data)
    
    # If both persons are same, randomize again.
    if personOne == personTwo:
        personTwo = random.choice(data)

    print(f"Compare A: {personOne["name"]}, {personOne["description"]}.\n{vs}")
    print(f"Against B: {personTwo["name"]}, {personTwo["description"]}.")

    result = checkAnswer(input("\nWho has more followers? Type 'A' or 'B': ").upper)
            
printLogo()
print(f"Sorry that's wrong. Final Score: {score}")