import time
import os
print ("******Welcome To Monoux Money Bank******")
time.sleep(1)
FirstName=input("Please enter your first name: ")
LastName=input("Please enter your Last name: ")
s=0
c=0
l=0
def Saving():
    print("We are now going to go through security procedures for the Savers account.")
    Address==str(input("Please enter the address which you are currently staying at: "))
    return (Address)

def Current():
    print("We are now going to go through security procedures for the Current account.")
    Address=str(input("Please enter the address which you are currently staying at: "))
    return (Address)

def Loan():
    print("We are now going to go through security procedures for the Loan account.")
    Address=str(input("Please enter the address which you are currently staying at: "))
    return (Address)
    
PreviousAccount=input("Have you had a previous account with us y/n: ")
if PreviousAccount =="y":
    AccountType = int(input("""Which type of account did you have
                                 1. Saving
                                 2. Current account
                                 3. Loan Account
                                  """))
    if AccountType == 1:
        s=1
    elif AccountType == 2:
        c=1
    else:
        l=1
    while s == 1 or c == 1 or l == 1:
        print ("You are not able to create the same account")
        Newaccount=int(input("""Which type of account would you like to set up
                                 1. Saving
                                 2. Current account
                                 3. Loan Account"""))
        while s == 1 or c == 1 or l == 1:
            if Newaccount ==1:
               if PreviousAccount==1:
                   s=1
               else :
                   s=0
            elif Newaccount ==2:
               if PreviousAccount==2:
                   c=1
               else :
                   c=0
            elif Newaccount ==3:
               if PreviousAccount==3:
                   l=1
               else :
                   l=0
        print ("Congratulations, your account has now been created! Thanks for banking with us.")
    
else:
    print("We will now take you through the process of setting up a new account.")
    Newaccount=int(input("""Which type of account would you like to set up
                                 1. Saving
                                 2. Current account
                                 3. Loan Account"""))
    if Newaccount == 1:
        print (Saving())
    elif Newaccount ==2:
        print(Current())
    else:
         print (Loan())
print("We are now storing the address")
global address
Data= open("Database.txt","w")
Data.write(str("Full name is "))
Data.write(FirstName)
Data.write(" ")
Data.write(LastName)
Data.write("\n")
Data.write("Student full address is ")
## Data.write(Address)
Data.close()
