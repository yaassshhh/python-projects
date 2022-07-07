# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:06:58 2022

@author: Yashraj Nigam
"""

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| |
| | . | 0 | = | | / | | 
| |___|___|___| |___| |  
|_____________________|
"""

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")


    more_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'new' to start a new calculation or type 'n' to stop: ")
    if more_calc == 'y':
      num1 = answer
    if more_calc == 'n':
      should_continue = False
      print(f"your answer is {answer}")
    else:
      should_continue = False
      print(f"your answer is {answer}")
      calculator()

calculator()