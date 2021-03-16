import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    name = input("Enter a word: ").upper()

    try:
        result = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()