from game_data import comparisions
import art
import random
import os

def ask_replay():
    while True:
        replay = input("Do you want to play the game? (y/n) ").lower()
        if replay == "y":
            return True
        if replay == "n":
            return False
        print("Please enter a valid letter.")

def get_user_input():
    while True:
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_input == "A":
            return True
        if user_input == "B":
            return False
        print("Please enter a valid letter.")

def get_game_data():
    random_number = random.choice(comparisions)
    return random_number

def compare_sides(side_A, side_B):
    user_input = get_user_input()
    if user_input:
        if side_A['name'] == side_B['name']:
            return "A"
        elif side_A['follower_count'] > side_B['follower_count']:
            return "A"
        else:
            return "C"
    else:
        if side_A['name'] == side_B['name']:
            return "A"
        elif side_B['follower_count'] > side_A['follower_count']:
            return "B"
        else:
            return "C"

def print_sides(side_A, side_B):
    print(art.logo)
    print(f"Compare A: {side_A['name']}, {side_A['description']}")
    print(art.vs)
    print(f"Against B: {side_B['name']}, {side_B['description']}")

def game_logic():
    side_A = get_game_data()
    side_B = get_game_data()
    print_sides(side_A, side_B)
    correct = compare_sides(side_A, side_B)
    score = 0
    while correct != "C":
        os.system("clear")
        score += 1
        print(f"You're right! Current score: {score}")
        if correct == "A":
            side_B = get_game_data()
            print_sides(side_A, side_B)
            correct = compare_sides(side_A, side_B)
        if correct == "B":
            side_A = side_B
            side_B = get_game_data()
            print_sides(side_A, side_B)
            correct = compare_sides(side_A, side_B)
    print(f"Sorry, that's wrong. Final score: {score}")
        
os.system("clear")
replay = ask_replay()
while replay:
    os.system("clear")
    game_logic()
    replay = ask_replay()