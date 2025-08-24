import random

word_list = ["Apple", "Orange", "Grape"]

def get_random_word():
    return list(random.choice(word_list))

print(*get_random_word())
