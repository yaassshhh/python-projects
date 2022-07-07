# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:19:58 2022

@author: Yashraj Nigam
"""
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
      
        
def check_ans(guess,answer,turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")

def game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1,100)
    print(answer)
    
    turns = difficulty()
    
    guess = 0
    while guess!= answer:
        print(f"You have {turns} attempts to guess the number.")
        
        guess = int(input("Make a guess: "))
        turns = check_ans(guess,answer,turns)
        
        
        if turns == 0:
          print("You've run out of guesses, you lose.")
          return
        elif guess != answer:
          print("Guess again.")
           
game()