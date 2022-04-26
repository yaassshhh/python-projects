# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:51:11 2021

@author: Yashraj Nigam
"""

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess < random_number:
            print("Sorry, guess again. too low.")
        elif guess > random_number:
            print("Sorry, guess again. too high.")
        
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")



guess(10)
