import random
import sys
word_list = ["aardvark", "baboon", "camel"]

def ask_letter():
    return input("Please enter a letter. ")

def get_random_word():
    return list(random.choice(word_list))

random_word = get_random_word()
user_guess = []
def draw_initial_lines():
    for _ in range(len(random_word)):
        user_guess.append("_")
    print(*user_guess)

def draw_guesses():
    guessed_letter = ask_letter()
    for i in range(len(random_word)):
        if random_word[i] == guessed_letter:
            user_guess[i] = guessed_letter
    print(*user_guess)
 
draw_initial_lines()
for _ in range(6):
    draw_guesses()
    if user_guess == random_word:
        print("You win!")
        sys.exit()
print("You lose")
