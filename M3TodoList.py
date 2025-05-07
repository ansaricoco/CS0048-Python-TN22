task_list = []

while True:
    print("Menu: \n")
    print("1 - Add Task: \n")
    print("2 - Remove Task: \n")
    print("3 - View Tasks: \n")
    print("4 - Exit: \n")
    opt = input("Enter your choice (1-4): ")
    if opt == "1":
        taskadd = input("Enter the task to add: ")
        task_list.append(taskadd)
        print ("Task added.")
    elif opt == "2":
        taskadd = input("Enter task to remove: ")
        found = False
        for i in task_list:
            if i == taskadd:
                found = True
                task_list.remove(taskadd)
                print ("Task removed.")
        if not found:
            print("Task not found")
        
    elif opt == "3":
        print("Task list: ")
        for i in task_list:
            print(i)
    elif opt == "4":
        print("Thank you. Exiting...")
        break
    else:
        print("Invalid input. Please try again")
    
    
