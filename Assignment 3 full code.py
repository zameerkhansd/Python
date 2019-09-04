import time
import os
import sys

def help():
    os.startfile ("help.txt")
    print(menu1())

def customerdetails():
    global name
    global lname
    global postcode
    global Contactnumber
    global emailaddress
    print("           Customer deatils ")
    name=input("Please enter your first name: ")
    lname=input("Please enter your Last name: ")
    postcode=input("Please enter your postcode: ")
    Contactnumber=int(input("Please enter your number : "))
    emailaddress=input("Plese enter your email address: ")
    print("Thank you for your contact information")
    return(menu1())

def Marquee():
    print ("             A Marquee")
    print("""1	Medium - £400 for day 1 and £180 for each additional day
             2	Large - £500 for day 1 and £200 for each additional day""")
    global Marq
    t=1
    while t == 1:
        Marq=int(input("Please enter the number for the Marquee you would like: "))
        global TotalMarq
        if Marq ==1:
            t=0
            days=int(input("Please enter how many days you would like the Marquee for: "))
            Total1=days-1
            TotalMarq= Total1*180+400
        elif Marq ==2:
            t=0
            days=int(input("Please enter how many days you would like the Marquee for: "))
            Total1=days-1
            TotalMarq= Total1*200+500
        else:
            print("Please try again")
            Marq=int(input("Please enter the number for the Marquee you would like: "))

        print("Your total for the Marquee is £",TotalMarq)
        return (menu1())
        

def Meals():
    print("                   Meals")
    print("""               Todays menu
1- Meat, £15.50 (Beef or chicken)
2- Fish, £13.95
3- Vegetarian, £10.00""")
    z=1
    global FinalOrder
    global FinalMoney
    while z == 1:
        food = int(input("Please enter the number you would like from the menu"))
        if food ==1:
            print("""Would you like
            1-beef
            2-Chicken """)
            food2 = int(input("Please enter the number fo the meat you would like: "))
            if food2 ==1:
                FinalOrder = "Meat, Beef"
                FinalMoney = 15.50
                print(FinalOrder)
                print(FinalMoney)
                z=0
            elif food2 ==2:
                FinalOrder= "Meat, Chicken"
                FinalMoney = 15.50
                print(FinalOrder)
                print(FinalMoney)
                z=0
        elif food ==2:
            FinalOrder = "Fish"
            FinalMoney = 13.95
            print(FinalOrder)
            print(FinalMoney)
            z=0
        elif food ==3:
            FinalOrder = "Vegetarian"
            FinalMoney = 10.00
            print(FinalOrder)
            print(FinalMoney)
            z=0
        else:
            ("Error, the number is incorrect, Please try again.")
            food = int(input("Please enter the number you would like from the menu"))
    return (menu1())

def menu1():
    print("""

    1.Customer details

    2.A Marquee

    3.Meals

    4.Print Invoice
    
    5.Exit """)
    global menu
    menu=int(input("Please enter a number from the menu: "))
    x=1
    while x == 1:
        if menu == 1:
            x=0
            print(customerdetails())
        elif menu == 2:
            x=0
            print(Marquee())
        elif menu == 3:
            x=0
            print(Meals())
        elif menu == 4:
            x=0
            print(PrintInvoice())
        elif menu == 5:
            x=0
            print (exit())
        else:
            print("Please try again")
            menu=int(input("Please enter a number from the menu: "))
    return ()

def PrintInvoice():
    global information
    information = ["The users full name is name" + " " + lname]
    address1= ["\n"+"Full postcode is: " + postcode]
    Contactinfo=["\n"+"Number - " + str(Contactnumber)+"\n"+"Email address is " +  emailaddress]
    data = open("Data.txt", "w")
    data.writelines(str(information))
    data.writelines(str(address1))
    data.writelines(str(Contactinfo))
    data.close()
    price = open("Price.txt", "w")
    price.write(str("Your total for the Marquee is £"))
    price.write(str(TotalMarq))
    price.write(str("\n" + "Your total for the food is £"))
    price.write(str(FinalMoney))
    TotalPrice1=TotalMarq+FinalMoney
    price.write(str("\n"+ "Your total price without VAT is £"))
    price.write(str(TotalPrice1))
    TotalAVat=TotalPrice1*1.20
    price.write(str("\n"+"Your total price with VAT is £"))
    price.write(str(TotalAVat))
    price.close()
    
    os.startfile("Price.txt","print")
    return(menu1())

def exit():
    sys.exit(0)
    return()
print("                                    Welcome to Zara's catering      ")
time.sleep(2)
help1=input("Would you like to open the help file? (y/n)")

if help1 == "y":
    print (help())
else:
    print(menu1())
