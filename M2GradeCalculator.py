subjects = []
scores = []
while True:
    
    print ("1. Add Score\n")
    print ("2. Calculate Average\n")
    print ("3. Exit")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        subject = input("Enter the subject: ")
        subjects.append(subject)
            
        score = int(input("Enter the score: "))
        scores.append(score)
        print("Score added. ")
    elif choice == "2":
        total = 0
        average = 0
        for score in scores:
            total+=score
        average = total/len(scores)
        print ("Average Grade: ", average)
    elif choice == "3":
        print("Thank you. Exiting...")
        break
    else:
        print("Invalid input. Please try again. ")
    
    
