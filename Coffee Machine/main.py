from data import MENU, resources
from art import logo

# Initial variables
cash = 0


def get_drinks():
    """Returns all available drinks in the machine."""
    drinks_in_machine = []
    for drink in MENU.items():
        drinks_in_machine.append(drink[0])
    return drinks_in_machine


def get_report():
    """Gets the resources available in the coffee machine."""
    return resources["water"], resources["milk"], resources["coffee"]


def check_resources(type_of_order):
    """Check if resources is available in the machine for the order."""
    avail_water, avail_milk, avail_coffee = get_report()
    if type_of_order == "espresso":
        if avail_water >= 50 and avail_coffee >= 18:
            return True
        else:
            return False
    elif type_of_order == "latte":
        if avail_water >= 200 and avail_coffee >= 24 and avail_milk >= 150:
            return True
        else:
            return False
    elif type_of_order == "cappuccino":
        if avail_water >= 250 and avail_coffee >= 24 and avail_milk >= 100:
            return True
        else:
            return False


def insert_coins():
    """Insert cash into the machine and return total cash inserted."""
    print("Please insert coins.")
    oneRupee = int(input("How many one rupees?: "))
    twoRupee = int(input("How many two rupees?: ")) * 2
    fiveRupee = int(input("How many five rupees?: ")) * 5
    tenRupee = int(input("How many ten rupees?: ")) * 10
    return oneRupee + twoRupee + fiveRupee + tenRupee


def sufficient_amount(type_of_order, amount):
    """Check if sufficient cash is inserted into the machine."""
    if type_of_order == "espresso":
        if amount >= MENU["espresso"]["cost"]:
            return True, amount - MENU["expresso"]["cost"]
        else:
            return False, 0
    elif type_of_order == "latte":
        if amount >= MENU["latte"]["cost"]:
            return True, amount - MENU["latte"]["cost"]
        else:
            return False, 0
    elif type_of_order == "cappuccino":
        if amount >= MENU["cappuccino"]["cost"]:
            return True, amount - MENU["cappuccino"]["cost"]
        else:
            return False, 0


def update_resources():
    """Update resources available in the coffee machine."""
    for drink, details in MENU.items():
        needed_water = details["ingredients"]["water"]
        needed_coffee = details["ingredients"]["coffee"]

        resources["water"] -= needed_water
        resources["coffee"] -= needed_coffee

        # If key 'milk' exist in dictionary only update
        if details.get("milk"):
            needed_milk = details["ingredients"]["milk"]
            resources["milk"] -= needed_milk


# Print logo
print(logo)

while True:
    # Get all drinks available in machine
    drinks = get_drinks()

    order = input(f"What would you like? ({'/'.join(drinks)}): ").lower()

    if order == "report":
        water, milk, coffee = get_report()
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {cash}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        resources_available = check_resources(order)
        # Check if resources available
        if resources_available:
            cash = insert_coins()
            amountSufficient, change = sufficient_amount(order, cash)
            # Check if cash inserted is sufficient
            if amountSufficient:
                print(f"Here is your {order}. Enjoy!\nHere is {change} in change.")
                # Updated the resources
                update_resources()
            else:
                print(f"Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources in the machine.")
            break
    elif order == "off":
        break
    else:
        print("Invalid order.")
