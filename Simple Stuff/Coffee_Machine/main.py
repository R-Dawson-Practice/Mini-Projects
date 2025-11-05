MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
RESOURCES = {"water": 300, "milk": 200, "coffee": 100}
UNITS = {"water": "ml", "milk": "ml", "coffee": "g"}


def display_report(profit):
    for resource, value in RESOURCES.items():
        unit = UNITS.get(resource, "")
        print(f"{resource.capitalize()}:{value} {unit}")
    print(f"Money: £{profit:.2f}")

def check_input(change):
    if change == "":
        return 0
    try:
        change = int(change)
        if change < 0:
            return None
        return change
    except ValueError:
        return None
    

change_value = {"quarters": 0.25, "nickel":0.05, "pennies":0.01}

def transaction(item):
    price = MENU[item]["cost"]
    print(f"{price:.2f}")
    print("Insert your coins")
    while True:
        quarters = input("How many quarters?: ")
        quarters = check_input(quarters)
        if quarters is None:
            print("Invalid quarters")
            continue
        
        nickels = input("How many nickels?: ")
        nickels = check_input(nickels)
        if nickels is None:
            print("Invalid nickels")
            continue

        pennies = input("How many pennies?: ")
        pennies = check_input(pennies)
        if pennies is None:
            print("Invalid pennies")
            continue
        total = ((change_value.get("quarters") * quarters) + (change_value.get("nickel") * nickels) + (change_value.get("pennies") * pennies))

        return total, price

def selection():
    options = "/".join(MENU)
    print(
        f"What would you like?: ({options})",
    )
    choice = input().strip().lower()

    if choice == "report":
        return "REPORT"
    elif choice in MENU:
        return choice
    elif choice == "exit":
        return "EXIT"
    else:
        return "INVALID"

def calculate(total, price):
    if total >= price:
        change = total - price
        return True, change
    else:
        return False, None
    
def update_resources(choice):
    ingredients = MENU.get(choice).get("ingredients")
    for resource, value in ingredients.items():
        RESOURCES[resource] -= value
        
def sufficient_resources(choice):
    ingredients = MENU.get(choice).get("ingredients")
    for resource, value in ingredients.items():
        if RESOURCES[resource] - value < 0:
            return False
        
    return True

def coffee_machine():
    profit = 0
    while True:
        choice = selection()
        if choice == "REPORT":
            display_report(profit)
            continue
        if choice == "EXIT":
            break
        if choice == "INVALID":
            print("Invalid Input")
            continue
        
        accepted = sufficient_resources(choice)
        if not accepted:
            print("Insufficient Resouces")
            continue
        total, price = transaction(choice)
        accepted, change = calculate(total, price)
        if accepted is False:
            print("Insufficient Funds")
        else:
            print(f"Your change is: £{change:.2f}")
            profit += price
            update_resources(choice)



def main():
    coffee_machine()

if __name__ == "__main__":
    main()
