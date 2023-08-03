import os

biddings = []
other_bidders = "Yes"

def winner(biddings):
    winner = ""
    bid_winner = 0
    for bidder in biddings:
        if bidder["bid"] > bid_winner:
            bid_winner = bidder["bid"]
            winner = bidder["name"]
    print("The winner is",winner)

while other_bidders == "Yes":
    def bidding():
        bidder = {}
        bidder["name"] = name_user
        bidder["bid"] = bid_user
        biddings.append(bidder)

        return bidder
    
    print("")
    print("Welcome to the blind auction program")
    name_user = input("What is your name: ")
    bid_user = int(input("What is your bid: "))
    bidder = bidding()

    bidder_confirm = input("Are there any other bidders? (Yes or no): ").lower()
    if bidder_confirm == "yes":
        os.system("clear")
    else:
        other_bidders = "No"
        winner(biddings)
