import game_data
from sys import exit

def ask_drink_type():
    while True:
        drink_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink_type in ("espresso", "latte", "cappuccino"):
            return drink_type
        elif drink_type == "off":
            exit()
        elif drink_type == "report":
            print_report()
            exit()
        print("Please enter a valid drink.")
    
def get_resources():
    return game_data.resources

def print_report():
    report = get_resources()
    print(f"Water: {report["water"]}ml")
    print(f"Milk: {report["milk"]}ml")
    print(f"Coffee: {report["coffee"]}g")
    print(f"Money: ${report["money"]}")

def print_out_of(resource):
    print(f"Sorry there is not enough {resource}.")

def check_enough_resources(drink_type):
    resources = get_resources()
    recipes = {
        "espresso": {"water": 50, "coffee": 18},
        "latte": {"water": 200, "coffee": 24, "milk": 150},
        "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
    }
    for ingredient, amount_needed in recipes.get(drink_type).items():
        if resources.get(ingredient, 0) < amount_needed:
            print_out_of(ingredient)
            return False
    return True

def get_coins_user():
    while True:
        coins = input("Please enter coins ('quarters', 'dimes', 'nickles', 'pennies') ")