def add(x,y):
    return x + y
    
def subtract(x,y):
    return x - y

def multiply(x,y):
    return x* y
    
def divide(x,y):
    return x/y
    
while True:
    print("Menu: \n")
    print("1 - Add: \n")
    print("2 - Subtract: \n")
    print("3 - Multiply: \n")
    print("4 - Divide: \n")
    print("5 - Exit: \n")
    opt = input("Enter your choice (1-5): ")
    if opt == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = add(num1,num2)
        print ("Result: ", result)
    elif opt == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = subtract(num1,num2)
        print ("Result: ", result)
    elif opt == "3":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = multiply(num1,num2)
        print ("Result: ", result)
    elif opt == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = divide(num1,num2)
        print ("Result: ", result)
    
    elif opt == "5":
        print ("Thank you.")
        break
    else:
        print("Invalid input. Please try again")
    
    