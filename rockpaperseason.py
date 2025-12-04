import random 
options = [ "Rock", "Paper", "Scissors"]
while True: 
    user = input("Input Rock/Paper/Scissors = ").upper()
    if user != input() :
        print("invalid input")
    computer = random.choice(options)
    print("Computer", computer)
    
    if user == computer:
        print("Draw")
    elif (user == "Rock" and computer == "Scissors") or \
    (user == "Paper" and computer == "Rock") or \
    (user == "Scissors" and computer == "Paper"):
        print("You won the game bro")
        
    else:
        print("You loose")
    
    play = input("Want to play again ? (Y/N)").upper()
    if play != "Y":
        print("Thanks for playing ")
        break
