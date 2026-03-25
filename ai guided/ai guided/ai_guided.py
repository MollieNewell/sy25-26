while True:
    day = input("what day would you like to see?: ").lower()

    with open(day + ".txt", "r") as file:  
        lines = file.read() 
        print(lines)

    edit = input("Would you like to add to your assignments? (yes or no): ").lower()

    if edit == "yes":
        day3 = input("what day would you like to add to?: ").lower()
        assignment = input("What assignment do you need to do?: ")

    if day3 == "monday":
        file = open("monday.txt","a")
        file.write(assignment + '\n') 

    elif day3 == "tuesday":
        file = open("tuesday.txt","a")
        file.write(assignment + '\n') 

    elif day3 == "wednesday":
        file = open("wednesday.txt","a")
        file.write(assignment + '\n') 

    elif day3 == "thursday":
        file = open("thursday.txt","a")
        file.write(assignment + '\n') 

    elif day3 == "friday": 
        file = open("friday.txt","a")
        file.write(assignment + '\n') 
    if edit == "no":
        break