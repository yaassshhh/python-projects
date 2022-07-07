# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 01:47:39 2022

@author: Yashraj Nigam
"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]

player = int(input("What do you chose? Type 0 for Rock, 1 for paper or 2 for scissors."))
print(game[player])

ran = random.randint(0,2)
com = game[ran]
print("Computer choose:"+com)
comp = int(ran)
if player == ran:
    print("Tied")
elif player == 0 & comp == 2 | player == 1 & comp== 0 | player == 2 & comp== 1 :
    print("You win")
else:
    print("You lose")