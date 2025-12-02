# A simple project to change Interactive String Manipulation Program 

name = str(input("Enter your name "))

print("Your name is = " , name)

print("What do you want to do eg- isalpha , isalnum , lower , upper , title , isupper ")

operation = input("Enter it = ")

if operation == 'lower': 
    
    print(name.lower())
    
elif operation == 'upper':
    
    print(name.upper())
    
elif operation == 'title':
    
    print(name.title())
    
elif operation == 'isupper':
    
    print(name.isupper())
    
elif operation == 'islower':
    
    print(name.islower())
    
    
    
    
    
    
    
