import random as rand
import os
import subprocess

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_deck(deck: list):
    total = 0
    for i in deck:
        total += i
    return total


def choose_hand(deck: list):
    card = rand.choice(cards)
    if card == 11 and (calculate_deck(deck) + card) > 21:
        card = 1
    deck.append(card)
    return deck


def start_game():
    player_deck = []
    dealer_deck = []

    player_deck = choose_hand(player_deck)
    player_deck = choose_hand(player_deck)

    dealer_deck = choose_hand(dealer_deck)

    print("Game Start")

    draw_phase = True
    while draw_phase is True and calculate_deck(player_deck) <= 21:
        os.system('cls' if os.name is 'nt' else 'clear')
        print(f"Your deck: {player_deck} Value: {calculate_deck(player_deck)} \nDealer's deck {dealer_deck}")
        if input(f"Do you want to draw a hand 'y' or fold 'n'\n") == "y":
            player_deck = choose_hand(player_deck)
        else:
            draw_phase = False

    dealer_deck = choose_hand(dealer_deck)

    player_total = calculate_deck(player_deck)

    if player_total > 21:
        print(
            f'''Your deck: {player_deck} Value: {calculate_deck(player_deck)} \n
            Dealer's deck {dealer_deck} Value: {calculate_deck(dealer_deck)}''')
        print("Bust! Dealer wins!")
        return

    while calculate_deck(dealer_deck) < 17:
        dealer_deck = choose_hand(dealer_deck)

    dealer_total = calculate_deck(dealer_deck)

    print(f"Your deck: {player_deck} Value: {player_total} \nDealer's deck {dealer_deck} Value: {dealer_total} ")

    if player_total == 21 and len(player_deck) == 2:
        print("Black Jack!!!")

    if dealer_total > 21:
        print("Dealer Bust! You win")
    else:
        if player_total > dealer_total:
            print("Player Wins!")
        elif dealer_total > player_total:
            print("Dealer Wins!")
        else:
            print("Draw!!")


while input("Do you want to play a game of Black Jack? Y/N \n").lower() == "y":
    start_game()
