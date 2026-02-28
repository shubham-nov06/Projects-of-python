import random

name = input("Enter your name ").lower()
number = random.randint(1, 99)
username = name + str(number)
print("Your username is :" ,username)
