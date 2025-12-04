import random 
options = [ "Rock", "Paper", "Scissors"]
while True: 
    user = input("Input Rock/Paper/Scissors")
    computer = random.choice(options)
    print("Computer",computer)
    
    if user==computer:
        print("Draw")
        
