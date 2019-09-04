print("Welcome to SGMC mobile services. ")
import time
print("If you would like to update your personal details please press 1.")
time.sleep(1)
print("If you would like to purchase a phone please press 2.")
time.sleep(1)
print("If you would like to purchase an accessorie press 3.")
time.sleep(1)
print("If you would like to update your payement details press 4.")
time.sleep(1)
print("If you would like to print a receipt please press 5.")
time.sleep(1)
print("If you would like HELP please press 6. ")
time.sleep(1)
option = int(input("Please enter the number number of the option: "))
### Done
if option == 1:
    name = input("Please enter your name: ")
    road = input("Please enter the name of the new road: ")
    door = int(input("Please enter the door number: "))
    age = int(input("Please enter your age: "))
    employement = input("Please enter your emloyement status: ")

    print("Thank you we will have your personal information updated! ")
### Done
elif option == 2:
    print("Here is our latest deals")
    print("Unlimited mins and unlimted text, 4GB data for £12, this is option 1")
    print("Unlimited mins and unlimted text, 12GB data for £22, this is option 2")
    print("400 mins and unlimted text, 6GB data for £12, this is option 3")
    print("Unlimited mins, 2000 text, 4GB data for £10, this is option 4")
    deal=int(input("Please enter the number from the deal you are interested in: "))
    if deal < 5 and deal >0:
        print("We will be updating your plan, thank you for your time. Have a nice day!")
    else:
        print("The number you have entered has caused an error, please try again later!")
### Done
elif option == 3:
    print ("We have three accessories in stock these include:")
    print("Headset £30, please press 1 ")
    time.sleep(0.5)
    print("Charger £10, pleae press 2")
    time.sleep(0.5)
    print("Earpods £20, please press 3")
    time.sleep(2)
    accessories = int(input("Please enter the number for the accessories you would like to purchase: "))
    if accessories == 1:
        print("We have successfully added the Headset to your basket.")
    elif accessories == 2:
        print("We have successfully added the Charger to your basket.")
    elif accessories ==3:
        print("We have successfully added the earpods to your basket.")
    else:
        print ("An error has occured please try again later")
### Done
elif option == 4:
    ccnumber = int(input("Please enter your card number: "))
    sortcode = int(input("Please enter your card sort code: ")) 
    accnumber = int(input("Please enter your card account number: ")) 
    cvv = int(input("Please enter the cvv (The last 3 digits at the back of the card): ")) 

### Text
##
##text = int(input("Please enter the amount of text you would like:  "))
##
##if text == 0:
##    print ("So you would like unlimited text, this will be noted.")
##    text =("Unlimited")
##    textprice = 5
##else:
##    print ("So you would like", text, " texts!")
##    if text < 1000:
##        textprice = 7
##    else:
##        textprice = 4
### Minute
##minutes = int(input("Please enter the amount of minutes you would like: "))
##
##if minutes == 0:
##    print ("So you would like unlimited minutes, this will be noted.")
##    minutes =("Unlimited")
##    minutesprice = 10
##else:
##    print ("So you would like", minutes, "minutes!")
##    if minutes < 1000:
##        minutesprice = 10
##    else:
##        minutesprice = 5
##elif option == 4:
##    print("hello4")
##elif option == 5:
##    print("hello 5")
##elif option == 6:
##    print("hello 6")
##else:
##    print("Please try again later.")
##
##import random
##    print (random.randint(0, 20))
##
