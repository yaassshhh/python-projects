# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:49:48 2022

@author: Yashraj Nigam
"""

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} with bid ${highest_bid}")


while not bidding_finished:    
    name = input("What is your name ?")
    price = int(input("What is your bid? $"))
    
    bids[name] = price
    
    more_bidder = input("Are there any other bidders? Type Yes or No.")
    if more_bidder == "Yes":
        bidding_finished = False
    else:
        bidding_finished = True
        highest_bidder(bids)









