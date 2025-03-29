import os

bids = {}

def add_bid():
    name = input("Enter your name: ")
    bid = round(float(input("Enter your bid: $")), 2)
    bids[name] = bid

def highest_bid(dictionary):
    high_bidder = ""
    high_bid = 0
    for name, bid in dictionary.items():
        if bid > high_bid:
            high_bidder = name
            high_bid = bid
    return high_bidder, high_bid

print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
""")

print("Welcome to the silent auction.")

while True:
    mode = input("Press '1' to add a bid, press '2' to finish: ")
    if mode != '1' and mode != '2':
        print("Invalid selection.")
    elif mode == '1':
        add_bid()
        os.system('clear')
    elif mode == '2':
        high_bidder, high_bid = highest_bid(bids)
        print(f"The winner is {high_bidder}, with a bid of ${high_bid:.2f}.")
        break