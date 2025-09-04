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
            continue
        print("Please enter a valid drink.")
    
def get_resources():
    return game_data.resources

def print_report():
    report = get_resources()
    print(f"Water: {report['water']}ml")
    print(f"Milk: {report['milk']}ml")
    print(f"Coffee: {report['coffee']}g")
    print(f"Money: ${report['money']}")

def print_out_of(resource):
    print(f"Sorry there is not enough {resource}.")

def check_enough_resources(drink_type):
    resources = get_resources()
    for ingredient, amount_needed in game_data.MENU.get(drink_type)["ingredients"].items():
        if resources.get(ingredient, 0) < amount_needed:
            print_out_of(ingredient)
            return False
    return True

def get_coins_user():
    while True:
        coin_type = input("Please enter coins ('quarter', 'dime', 'nickel', 'pennie', 'dollar') and 'stop' to end: ").lower()
        if coin_type in {"quarter", "dime", "nickel", "pennie", "dollar", "stop"}:
            return coin_type
        print("Please enter a valid coin")

def insert_coins():
    coin_dict = {
        "pennie" : 0.01,
        "dime" : 0.10,
        "nickel" : 0.05,
        "quarter" : 0.25, 
        "dollar" : 1.00,
    }
    total_count = 0
    keep_adding = get_coins_user().lower()
    while keep_adding != "stop":
        for coin_type in coin_dict:
            if keep_adding == coin_type:
                total_count += coin_dict[coin_type]
        keep_adding = get_coins_user()
    return total_count

def check_cost(user_money, drink_type):
    menu = game_data.MENU
    if user_money < menu[drink_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if user_money > menu[drink_type]["cost"]:
        print(f"Here is {user_money - menu[drink_type]["cost"]} in change")
    game_data.resources["money"] += menu[drink_type]["cost"]
    return True

def take_from_resources(drink_type):
    menu = game_data.MENU
    for i in game_data.resources:
        if i != "money":
            game_data.resources[i] = game_data.resources[i] -  game_data.MENU[drink_type]["ingredients"][i]

def print_goodbye(drink_type):
    print(f"Here is your {drink_type}. Enjoy!")


drink_type = None
while drink_type != "off":
    drink_type = ask_drink_type()
    resources_available = check_enough_resources(drink_type)
    if resources_available:
        get_coins_user()
        user_money = insert_coins()
        money_available = check_cost(user_money, drink_type)
        if money_available:
            take_from_resources(drink_type)
            print_goodbye(drink_type)