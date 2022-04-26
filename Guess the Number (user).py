# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 23:55:46 2021

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
    
def computer_guess(x):
    l = low = 1
    h = high = x 
    feedback = ""
    while feedback != "c":
        if low!= high:
            guess = random.randint(low,high)
        else: 
            guess = low
        feedback = input(f"Is {guess} too high {h}, too low {l}, or correct??")
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1
    
    print(f"yay! The computer guessed your number {guess},correctly!")
    
computer_guess(10)