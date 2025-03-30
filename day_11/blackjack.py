import random
import string

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
running_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
player_hand = []
dealer_hand = []


def opening_deal():
    for i in range(0, 2):
        card = random.choice(running_deck)
        player_hand.append(card)
        running_deck.remove(card)

    for i in range(0, 2):
        card = random.choice(running_deck)
        dealer_hand.append(card)
        running_deck.remove(card)

def deal(hand):
    card = random.choice(running_deck)
    hand.append(card)
    running_deck.remove(card)

def hand_count(hand):
    count = 0
    aces = 0
    for card in hand:
        if card == 'A':
            count += 1
            aces += 1
        elif card in string.digits or card == '10':
            count += int(card)
        elif card in ['J', 'Q', 'K']:
            count += 10
    if aces > 0 and count + 10 <= 21:
        count += 10
    return count


def blackjack_check(hand):
    has_ace = 'A' in hand
    has_ten_value = any(card in ['10', 'J', 'Q', 'K'] for card in hand)
    return has_ace and has_ten_value

print("""
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
""")

print(""""
                            _____           
                    _____  |K  WW|          
            _____  |Q  ww| | ^ {)|                 
     _____ |J  ww| | ^ {(| |(.)%%| _____
    |10 ^ || ^ {)| |(.)%%| | |%%%||A .  |
    |^ ^ ^||(.)% | | |%%%| |_%%%>|| /.\ |
    |^ ^ ^|| | % | |_%%%O|        |(_._)|
    |^ ^ ^||__%%[|                |  |  |
    |___0I|                       |____V|
                               
""")

opening_deal()
print(f"Your hand: {' '.join(player_hand)}\n")
print(f"Dealer's hand: {dealer_hand[0]} ?\n")

if blackjack_check(player_hand) and blackjack_check(dealer_hand):
    print(f"Dealer's hand: {' '.join(dealer_hand)}")
    print("Player and dealer both have Blackjack! Draw.")
elif blackjack_check(player_hand) and not blackjack_check(dealer_hand):
    print("Blackjack! Player wins.")
elif blackjack_check(dealer_hand) and not blackjack_check(player_hand):
    print(f"Dealer's hand: {' '.join(dealer_hand)}")
    print("Dealer has Blackjack! Dealer wins.")
print(f"Total: {hand_count(player_hand)}\n")

while True:
    if hand_count(player_hand) > 21:
        print("Player busts!\n")
        print(f"Dealer's hand: {' '.join(dealer_hand)}")
        input("")
        break
    decision = input("Press 'h' to hit, or 's' to stand: ")
    if decision not in ['h', 's']:
        print("Invalid selection.")
        input("")
    elif decision == 'h':
        deal(player_hand)
        print(f"\nYour hand: {' '.join(player_hand)}\n")
        print(f"Total: {hand_count(player_hand)}\n")
    elif decision == 's':
        print(f"\nPlayer stood on {hand_count(player_hand)}\n")
        print(f"Dealer's hand: {' '.join(dealer_hand)}")
        input("")
        break

if hand_count(dealer_hand) > 16:
    print(f"Total: {hand_count(dealer_hand)}")

while hand_count(dealer_hand) <= 16:
    deal(dealer_hand)
    print(f"Dealer's hand: {' '.join(dealer_hand)}")
    print(f"Total: {hand_count(dealer_hand)}")
    if hand_count(dealer_hand) <= 16:
        input("")

print(f"\nDealer's final hand: {' '.join(dealer_hand)}")
print(f"Dealer's total: {hand_count(dealer_hand)}")

input("")

if hand_count(player_hand) == hand_count(dealer_hand):
    print(f"Dealer and player both stood on {hand_count(player_hand)}! Hand is a draw.")
elif hand_count(player_hand) > 21:
    print("Dealer wins!")
elif hand_count(player_hand) > hand_count(dealer_hand) and not hand_count(player_hand) > 21:
    print("Player wins!")
elif hand_count(player_hand) < hand_count(dealer_hand) and not hand_count(dealer_hand) > 21:
    print("Dealer wins!")
elif hand_count(dealer_hand) > 21 and not hand_count(player_hand) > 21:
    print("Dealer busts!")

