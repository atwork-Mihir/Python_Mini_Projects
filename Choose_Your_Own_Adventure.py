# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:07:23 2024

Choose_Your_Own_Adventure

@author: Mihir Patil
"""
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()
    
    if answer == "swim":
        print("You swam accross and were eaten by a tiger.")
        
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
        
    else:
        print("Not a valid option. You lose. ")
        
elif answer == "right":
    
    answer = input("You come to a bridge it looks grumpy. Would you like to cross it or head back. Choose between 'Cross' or 'Back'. ").lower()
    
    if answer == "back":
        print("You go back and lose")
        
    elif answer == "cross":
        answer = input("You cross the bridge and meet a strangers. Do you talk to them (yes), (no)? ").lower()
        
        if answer == "yes":
            print("You talk to the strangers and they give you gold. Hurray! You win! :) !")
        elif answer == "no":
            print("You ignore the strangers and lose.")
        else:
            print("Not a valid option you lose.")
    else:
        print()
    print()
    
else:
    print("Not a valid option. You Lose.")
    
    


