# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:02:21 2022

@author: Yashraj Nigam
"""

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")

a= int(percentage_tip)
b= float(total_bill)

percentage = (((a/ 100)*b)+b)
c = int(percentage)

split = input("How many people to split the bill?")
d=int(split)

result = c/d
e=round(result,2)
print(f"Each person should pay: ${e}")
