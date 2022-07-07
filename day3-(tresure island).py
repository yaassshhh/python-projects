# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 04:20:59 2022

@author: Yashraj Nigam
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
c1= input("You are at a cross road. Where do you want to go? L OR R ")
if c1 == "L":
    c2= input("You came to a lake. There is an island in the middle of the lake. Type W to wait, type S to swim across ")
    if c2 == "W":
        c3 = input("You arrived at the island.There is a house with 3 doors. One red , one yellow , and one blue. Which colour do you choose? R,Y,B ")
        if c3 == "B":
            print("You win!")
        else:
            print("You lose!")
    elif c2 == "S":
            print("You lose!")
elif c1 == "R":
    c4 = input("You arrived at the island.There is a house with 3 doors. One red , one yellow , and one blue. Which colour do you choose? R,Y,B ")
    if c4 == "Y":
        c5 = input("You came to a lake. There is an island in the middle of the lake. Type W to wait, type S to swim across ")
        if c5 == "S":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("You lose!")

    


