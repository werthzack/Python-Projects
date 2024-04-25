import os

still_accepting = True

Offers = {}

while still_accepting == True:
    Name = input("What's your name? \n")
    Offer = input("What's your offer? \n")
    Offers[Name] = Offer
    os.system('cls' if os.name == 'nt' else 'clear')
    still_accepting = True if input("Is there any other buyer? Y/N ") == "Y" else False

highest_offer = 0
highest_bidder = ""
for name,offer in Offers.items():
    conv_offer = float(offer.replace("$",""))
    if conv_offer > highest_offer:
        highest_bidder = name
        highest_offer = conv_offer

print(f"{highest_bidder} wins the auciton with a bid of {highest_offer}")