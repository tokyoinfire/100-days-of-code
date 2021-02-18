import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

name = input("Enter a word: ").upper()
result = [nato_dict[letter] for letter in name]

print(result)
