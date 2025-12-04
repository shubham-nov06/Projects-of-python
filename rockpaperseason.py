import random 
options = [ "Rock", "Paper", "Scissors"]
while True: 
    user = input("Input Rock/Paper/Scissors")
    computer = random.choice(options)
    print("Computer",computer)
    
    if user==computer:
        print("Draw")
    elif (user=="Rock" and computer=="Secssors") or \
    (user== "Paper" and computer=="Rock") or \
    (user == "Scissors" and computer=="Paper"):
        print("You won the game bro")
else :
    print("You loose")
    play = input("Want to play again ? ").lower()

    if play!= "Y":
    break