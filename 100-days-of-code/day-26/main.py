import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

letter_dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_word = input("Please enter a word: ").upper()
nato_code = [letter_dict[_] for _ in user_word]

print(nato_code)

nato_code = [nato_code for _ in user_word]