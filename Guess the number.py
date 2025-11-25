# Just a simple guess  the number project 

import random 

number = random.randint(1, 100)

guess = 0 

while guess != number:
    
    guess = int(input("Guess a number between 1-100 = "))
    
    if guess < number: 
        
        print("Guess larger number = ")
        
    elif guess > number:
        
        print("Guess smaller number = ")
        
    elif guess == number:
        
        print("Good you guessed the right number ")
    
