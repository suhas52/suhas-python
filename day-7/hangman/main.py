import random
import sys
import lists

def ask_letter():
    return input("Please enter a letter: ")

def get_random_word():
    return list(random.choice(lists.word_list))

def draw_initial_lines(random_word):
    for _ in range(len(random_word)):
        user_guess.append("_")
    print(''.join(user_guess))
    return user_guess

def draw_guesses(life):
    guessed_letter = ask_letter()
    if guessed_letter in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guessed_letter:
                user_guess[i] = guessed_letter
    else:
        life -= 1
    draw_hangman(life)
    print(''.join(user_guess))
    return life

def draw_hangman(life):
    print(lists.stages[6 - life])

def retry_logic():
    choice = "x"
    while choice != "y" and choice != "n":
        choice = input ("Would you like to try again? (y/n) ")
        if choice == "y":
            return True
        if choice == "n":
            return False
        
retry = True
while retry == True:
    life = 7
    random_word = get_random_word()
    user_guess = []
    user_guess = draw_initial_lines(random_word)
    while True:
        life = draw_guesses(life)
        if user_guess == random_word:
            print("You win!")
            retry = retry_logic()
            break
        if life <= 0:
            print(f"You lose! The correct word was {''.join(random_word)}.")
            retry = retry_logic()
            break
print("Thank you for playing!")
