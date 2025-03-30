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

def player(player_hand):
    player_count = hand_count(player_hand)
    while True:
        if player_count > 21:
            print("Player busts!\n")
            input("")
            return player_count
        decision = input("Press 'h' to hit, or 's' to stand: ")
        if decision not in ['h', 's']:
            print("Invalid selection.")
            input("")
        elif decision == 'h':
            deal(player_hand)
            print(f"\nYour hand: {' '.join(player_hand)}\n")
            player_count = hand_count(player_hand)
            print(f"Total: {player_count}\n")
        elif decision == 's':
            print(f"\nPlayer stood on {player_count}\n")
            input("")
            return player_count

def dealer_play(dealer_hand):
    print(f"Dealer's hand: {' '.join(dealer_hand)}")
    input("")
    dealer_count = hand_count(dealer_hand)
    if dealer_count > 16:
            return dealer_count

    while dealer_count <= 16:
        deal(dealer_hand)
        dealer_count = hand_count(dealer_hand)
        print(f"Dealer's hand: {' '.join(dealer_hand)}\n")
        print(f"Total: {dealer_count}\n")
        if dealer_count <= 16:
            input("")
            
    return dealer_count

def blackjack_check(hand):
    has_ace = 'A' in hand
    has_ten_value = any(card in ['10', 'J', 'Q', 'K'] for card in hand)
    return has_ace and has_ten_value

def player_dealer_blackjack(player_hand, dealer_hand):
    if blackjack_check(player_hand) and blackjack_check(dealer_hand):
        print(f"Dealer's hand: {' '.join(dealer_hand)}")
        print("Player and dealer both have Blackjack! Draw.")
        return True
    elif blackjack_check(player_hand) and not blackjack_check(dealer_hand):
        print("Blackjack! Player wins.")
        return True
    elif blackjack_check(dealer_hand) and not blackjack_check(player_hand):
        print(f"Dealer's hand: {' '.join(dealer_hand)}\n")
        print("Dealer has Blackjack! Dealer wins.")
        return True
    return False

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
                                             888P                                  
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

while True: # Begin game loop
    opening_deal()
    print(f"Your hand: {' '.join(player_hand)}\n")
    input("")
    print(f"Dealer's hand: {dealer_hand[0]} ?\n")

    blackjack_happened = player_dealer_blackjack(player_hand, dealer_hand)

    if not blackjack_happened:
        print(f"Total: {hand_count(player_hand)}\n")

        player_count = player(player_hand)

        dealer_count = dealer_play(dealer_hand)

        print(f"Player total: {player_count} // Dealer total: {dealer_count}")
        input("")

        if player_count == dealer_count:
            print(f"Dealer and player both stood on {hand_count(player_hand)}! Hand is a draw.")
        elif player_count > 21:
            print("Player busted, dealer wins!")
        elif player_count > dealer_count:
            print("Player wins!")
        elif dealer_count > 21 and not player_count > 21:
            print("Dealer busted, player wins!")
        elif player_count < dealer_count:
            print("Dealer wins!")
    

    another_hand = input("Press 'enter' to play again, or type 'q' to quit: ")
    if another_hand == 'q':
        break
    else:
        player_hand = []
        dealer_hand = []
        running_deck = deck
