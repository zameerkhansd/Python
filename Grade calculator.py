import sys
import time
program = 0
#While loop for the program
while program == 0:
    x = 1
    Modules = int(input("Please enter the amount of Units you are doing:"))
    Modules2 = Modules
    TotalPoints = 0
    while x == 1:
        # Entering the grades
        grade=input("Please enter the grade which you have achieved")
        if grade == "D":
            points = 90
        elif grade == "M":
            points = 80
        elif grade == "P":
            points = 70
        elif grade == "d":
            points = 90
        elif grade == "m":
            points = 80
        elif grade == "p":
            points = 70
        Modules = Modules -1
        TotalPoints = TotalPoints + points
        if Modules == 0:
            x = 0
# Working out the distinction grades
    print (TotalPoints)
    MaxPoints = Modules2 * 90
    d1 = Modules2 * 0
    dm = Modules2 * 5
    m1 = Modules2 * 10
    mp = Modules2 * 15
    p1 = Modules2 * 20
    Distinction  = MaxPoints - d1
    DistinctionMerit = MaxPoints - dm
    Merit = MaxPoints - m1
    MeritPass = MaxPoints - mp
    Pass = MaxPoints - p1
    
# Printing the final grade
    if TotalPoints >= Distinction:
        print("You final grade is D*D*")
    elif TotalPoints >=DistinctionMerit:
        print ("You final grade is DM")
    elif TotalPoints >=Merit:
        print ("Your final grade is MM")
    elif TotalPoints >=Pass:
        print ("Your final grade is PP")
    Loop = input("Would you like to try again? y/n")
    x1 = 1
    while x1 == 1:
        if Loop == "y":
            print("Please be patient while the program restarts.")
            time.sleep(1)
            x1 = 0
            #program = 0
        elif Loop == "n":
            x1 = 0
            sys.exit()
            
