from art import logo
import random
cards = {
    "Ace" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "Jack" : 10,
    "Queen" : 10,
    "King" : 10,
} 

def ask_retry():
    while True:
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if choice == "y":
            return True
        if choice == "n":
            return False
        print("Please enter a valid choice")

def initilize_lists(player_list, cpu_list):
    for i in range(2):
        draw_card(player_list)
        draw_card(cpu_list)
    print(f"Your cards are: {player_list}, current score: {sum(player_list)}")
    print(f"Computer's first card: {cpu_list[0]}.")

def pick_another_card():
    while True:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "y":
            return True
        if choice == "n":
            return False
        print("Please enter a valid choice")

def draw_card(added_list):
    added_list.append(list(cards.values())[random.randint(0, 11)])

def evaluate_game(player_sum, cpu_sum):
    if player_sum > 21:
        print("You went over. You lose.")
    elif cpu_sum > 21:
        print("Computer went over. You win.")
    elif player_sum > cpu_sum:
        print("You win.")
    elif player_sum < cpu_sum:
        print("You lose.")
    else:
        print("It's a draw.")

def game_logic():
    player_list = []
    cpu_list = []
    initilize_lists(player_list, cpu_list)

    while sum(player_list) <= 21:
        another_card = pick_another_card()
        if another_card:
            draw_card(player_list)
            print(f"Your cards are {player_list}, current score: {sum(player_list)}")
        else:
            break   # player stands

    while sum(cpu_list) <= 17:
        draw_card(cpu_list)

    print(f"\nYour final hand: {player_list}, total: {sum(player_list)}")
    print(f"Computer's final hand: {cpu_list}, total: {sum(cpu_list)}")
    evaluate_game(sum(player_list), sum(cpu_list))
    

retry = ask_retry()
while retry:
    game_logic()
    retry = ask_retry()