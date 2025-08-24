import random

def get_random_number():
    return random.randint(0, 100)

def get_difficulty():
    difficulty = input("Please enter 1 for easy mode and 2 for hard mode: ") == "1"
    if difficulty == "1":
        return True
    if difficulty == "2":
        return False
    
def get_user_guess():
    return input("Please enter your guess between 0 and 100: ")

def check_high_low(generated_number, user_guess):
    if user_guess < generated_number:
        print("Your guess was too low.")
        return True
    elif user_guess > generated_number:
        print("Your guess was too high.")
        return True
    elif user_guess == generated_number:
        print("You win!")
        return False

def replay_logic():
    loop = True
    while loop:
        replay = input("Do you want to play the game? (y/n): ").lower()
        if replay == "y":
            return True
        if replay == "n":
            return False
        print("Please enter a valid letter. (y/n)")

replay = replay_logic()
while replay:
    generated_number = get_random_number()
    difficulty = get_difficulty()
    if difficulty:
        for i in range(10):
            user_guess = get_user_guess()
            if check_high_low(int(generated_number), int(user_guess)):
                continue
            else:
                break
    else:
        for i in range(5):
            user_guess = get_user_guess()
            if check_high_low(int(generated_number), int(user_guess)):
                continue
            else:
                break
    replay = replay_logic()
