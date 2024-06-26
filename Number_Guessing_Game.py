# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:19:31 2024

@author: Mihir Patil
"""

import random
import sys

top_of_range = input("Type a number:\n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        sys.exit()
else:
        print("Please type a number next time.")
        sys.exit()
        


random_number = random.randint(0, top_of_range)
# print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess) 
        
    else:
        print("Please type a number next time.")
        continue
    print("after continue")
    
    if user_guess ==  random_number:
        print("Your guess is correct.")
        break
    elif user_guess > random_number:
        print("Your guess is above the number")
    else:    
        print("Your guess is below the number")

print(f"You got it in {guesses} guesses.")

