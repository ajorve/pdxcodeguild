"""
Make a function that advises a player on the best next move in a round of blackjack.
For now, just use 15 as a Hit/Stay Threshold.  Feel free to add testable features.

>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player('A', 'A')
12 Hit.

>>> advise_player('J', 'K')
20 Stay.

"""


def advise_player(card1, card2):
    deck = {'A': 11, 'K': 10, 'Q': 10, 'J': 10}

    number_of_aces = 0
    hand_value = 0

    if isinstance(card1, str):
        if card1 == 'A':
            number_of_aces += 1
        card1 = deck[card1]

    if isinstance(card2, str):
        if card2 == 'A':
            number_of_aces += 1
        card2 = deck[card2]


    if number_of_aces == 2:
        hand_value = 12

    else:
        hand_value = card1 + card2

    if hand_value == 21:
        print(f"{hand_value} Blackjack!")

    elif hand_value > 15:
        print(f"{hand_value} Stay.")

    else:
        print(f"{hand_value} Hit.")
