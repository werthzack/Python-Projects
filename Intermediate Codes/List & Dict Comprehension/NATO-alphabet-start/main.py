import pandas

alphabet_data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in alphabet_data_frame.iterrows()}

def main():
    try:
        name = input("What's your name?").upper()
        nato_list = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        main()
    else:
        print(nato_list)

main()
