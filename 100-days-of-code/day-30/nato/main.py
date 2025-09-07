import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

letter_dict = {row.letter:row.code for (index, row) in df.iterrows()}


def generate():
    user_word = input("Please enter a word: ").upper()
    try:
        nato_code = [letter_dict[_] for _ in user_word]
    except KeyError:
        print("\nPlease enter a valid letter")
        generate()
    else:
        print(nato_code)


generate()