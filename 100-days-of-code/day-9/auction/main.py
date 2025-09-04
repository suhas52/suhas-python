def get_name():
    return input("Please enter your name: ").title()

def get_money():
    return int(input("How much do you want to put towards the auction? "))

def keep_going():
    while True:
        ch = input("Do new bits need to be added? (y/n)").lower()
        if ch == "y":
            return True
        if ch == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")
    
  
def add_to_dictionary(name, money, final_dict):
    final_dict[name] = money

def check_highest_bid(final_dict):
    highest_bidder = max(final_dict, key = final_dict.get)
    highest_bid = final_dict[highest_bidder]
    print(f"The highest bidder is {highest_bidder} and their bid is {highest_bid}")

retry = True
final_dict = {}
while retry:
    name = get_name()
    money = get_money()
    add_to_dictionary(name, money, final_dict)
    retry = keep_going()

check_highest_bid(final_dict)
