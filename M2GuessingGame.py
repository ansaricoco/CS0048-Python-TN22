import random
while True:
    guess_number = random.randrange(100)
    print ("1. Play Number Guessing Game\n")
    print ("2. Exit")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        counter = 0
        while True: 
            guess = int(input("Guess the number (1-100): "))
            counter += 1
            if guess == guess_number:
                print(f"Congratulations! You guessed the number in {counter} attempts.")
                break
            elif guess < guess_number:
                print("Too low! ")
            elif guess > guess_number:
                print("Too high! ")
            
            
    elif choice == "2":
        print("Thank you. Exiting...")
        break
    else:
        print("Invalid input. Please try again. ")
    
    
