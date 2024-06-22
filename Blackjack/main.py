############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

# Initial variables.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cardsHuman = []
cardsComputer = []
computerContinue = True
anotherCard = "y"
humanWentOver = False

def buildStartingDeck():
    """This function builds the starting deck for both the human player and computer. Each will get two cards inititally."""
    for _ in range(2):
        cardsHuman.append(random.choice(cards))
        cardsComputer.append(random.choice(cards))

def printCards(cardsHuman, cardsComputer):
    """Prints all cards of human player & first card of computer."""
    print(f"\tYour cards: {cardsHuman}, current score: {sum(cardsHuman)}\n\tComputer's first card: {cardsComputer[0]}")

def processCards(cardsHuman, cardsComputer):
    """Process the cards to check if anyone has won the game yet."""
    if sum(cardsHuman) > 21:
        print(f"\tYour final hand: {cardsHuman}, final score: {sum(cardsHuman)}\n\tComputer's final card: {cardsComputer}, final score: {sum(cardsComputer)}\nYou went over. You lose")
        return True

    elif sum(cardsComputer) > 21:
        print(f"\tYour final hand: {cardsHuman}, final score: {sum(cardsHuman)}\n\tComputer's final card: {cardsComputer}, final score: {sum(cardsComputer)}\nComputer went over. You win")
        return True

    elif continueBlackjack == 'n' and not computerContinue:
        print(f"\tYour final hand: {cardsHuman}, final score: {sum(cardsHuman)}\n\tComputer's final hand: {cardsComputer}, final score: {sum(cardsComputer)}")
        if sum(cardsHuman) > sum(cardsComputer):
            print("Win with a Blackjack")
            
        elif sum(cardsHuman) < sum(cardsComputer):
            print("You lose")
            
        else:
            print("Draw")

# Print Blackjack logo.
print(logo)

continueBlackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# Build starting deck.
buildStartingDeck()

# Loop until both human player or computer does not want to draw a card.
# Also, till human player score is less than or equal to 21.
while (continueBlackjack == "y" or computerContinue) and not humanWentOver:

    if continueBlackjack == "y":
        printCards(cardsHuman, cardsComputer)

    if anotherCard == "y":
        anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")

    if anotherCard == "y":
        cardsHuman.append(random.choice(cards))
        humanWentOver = processCards(cardsHuman, cardsComputer)
    else:
        continueBlackjack = 'n'
        processCards(cardsHuman, cardsComputer)

    # If human player score is less than or equal to 21.
    if not humanWentOver:
        if computerContinue:
            # This checks whether the computer want to draw a card or not.
            computerContinue = bool(random.randint(0, 1))
            if computerContinue:
                cardsComputer.append(random.choice(cards))
                if processCards(cardsHuman, cardsComputer):
                    computerContinue = False
            else:
                computerContinue = False
                processCards(cardsHuman, cardsComputer)
                
# Completed with dificulty EXPERT!!!. Had to use VSCode for debugging though.