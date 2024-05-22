import pandas

alphabet_data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in alphabet_data_frame.iterrows()}

name = input("What's your name?").upper()
nato_list = [nato_dict[letter] for letter in name]

print(nato_list)
