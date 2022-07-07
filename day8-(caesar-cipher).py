# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 01:43:39 2022

@author: Yashraj Nigam
"""
def encrypt(plain_text,shift_amt):
    
    cipher_text = ""
    
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amt
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)
    

def decrypt(plain_text,shift_amt):
    
    cipher_text = ""
    
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amt
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)
    
#if direction == "encode":
#    encrypt(text, shift)
#else:
#    decrypt(text, shift)
    
    
    
#OR COMBINE BOTH FUNCTIONS INTO ONE
def caesar(start_text, shift_amount, cipher_direction):
    
  end_text = ""
  
  if cipher_direction == "decode":
      shift_amount *= -1
  for char in start_text:
     if char in  alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
     else:
        end_text += char
    
    
  print(f"Here's the {direction}d result: {end_text}")

again = True
while again:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    caesar(text,shift,direction)
    
    result = input("Type Yes if You want to continue , otherwise type No")
    
    if result == "no":
        print("goodbye")
        again = False
        
        
    
