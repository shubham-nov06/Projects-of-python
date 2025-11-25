# A simple project of temperature convertor 

print(" 1 - Celsius to Fahrenheit ")

print(" 2 - Fahrenheit to Celsius ")

ch = int(input("Choose the option"))

if ch == 1:
    
    c = float(input("Celcius"))
    
    print("Fahrenheit = " , (c * 9 / 5) + 32)
    
elif ch == 2:
    
    f = float(input("Fahrenheit"))
    
    print("Celcius = " , (f - 32) * 5 / 9)
