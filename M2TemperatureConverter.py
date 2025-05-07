def ctof(x):
    return (x*9/5) + 32
    
def ftoc(x):
    return 5/9*(x-32)

while True:
    print("Menu: \n")
    print("1 - Celsius to Fahrenheit: \n")
    print("2 - Fahrenheit to Celsius: \n")
    print("3 - Exit: \n")
    opt = input("Enter your choice (1-3): ")
    if opt == "1":
        num1 = int(input("Enter temperature in Celsius: "))
        result = ctof(num1)
        print ("Temperature in Fahrenheit: ", result)
    elif opt == "2":
        num1 = int(input("Enter temperature in Fahrenheit: "))
        result = ftoc(num1)
        print ("Temperature in Celsius: ", result)
    elif opt == "3":
        print("Thank you")
        break
    else:
        print("Invalid input. Please try again")
    
    