import random
word_list = ["aardvark", "baboon", "camel"]

def get_word():
    return random.choice(word_list)
def get_guess():
    return input("Please enter a letter. ")

def draw_lines():
    for _ in word:
        if guess == _:
            print(_, end = "")
        else:
            print("_", end = "")

word = get_word()
guess = get_guess()
for _ in range(7):
    draw_lines()
