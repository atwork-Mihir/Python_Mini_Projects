# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:11:23 2024

@author: Mihir Patil
"""        

print("Welcome to my computer Quiz!")

playing = input("Do you want to play? \n") 
playing = playing.lower()
score = 0
if playing == "yes":
    print("OKAY! Let's play. :) ")
     
    answer = input("1) What does CPU stand for? \n") 
    answer = answer.lower()
    
    if answer == "central processing unit":
        print("Correct! You win\n")
        score += 1
    else:
        print("Incorrect!\n")
        
    answer = input("2) What does GPU stand for? \n") 
    answer = answer.lower()
    
    if answer == "graphics processing unit":
        print("Correct! You win\n")
        score += 1
    else:
        print("Incorrect!\n")
    
    answer = input("3) What does RAM stand for? \n") 
    answer = answer.lower()
    
    if answer == "random access memory":
        print("Correct! You win\n")
        score += 1
    else:
        print("Incorrect!\n")
        
    answer = input("4) What does PSU stand for? \n") 
    answer = answer.lower()
    
    if answer == "power supply":
        print("Correct! You win. \n")
        score += 1
    else:
        print("Incorrect!\n")
    
    if score > 2: 
        print(f"You got {score} question correct! Hurray!")
        print("You got" +" "+ str((score/4)*100) + "%.")
    else:
        print(f"You got {score} questions correct! Better luck next time.")
        print("You got" +" " +str((score/4)*100) + "%.")
        
elif playing == "no":
    print("Thank you very much for your time.\n")
    
    
else:
    print("Invalid Input")
   
    



    



