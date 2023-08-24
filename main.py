from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
auction_bids = {}
further_bids = True
while further_bids:
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: £"))
    auction_bids[name] = bid
    persons = input("Are there more bidders? Please enter yes or no: ").lower()
    clear()
    if persons == "no":
        further_bids = False

max_bid = max(auction_bids, key=auction_bids.get)
max_value = max(auction_bids.values())
print(f"The winner is: {max_bid} with a bid of {max_bid} £{max_value}")
