from art import logo
from replit import clear

print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
bidding_start = True
while bidding_start:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == 'no':
        bidding_start = False
    elif should_continue == 'yes':
        clear()

find_highest_bidder(bids)