import time
import os

def help():
    os.startfile ("HelpFile.txt")

print("Welcome to Sunny Villa")
time.sleep(2)
print("The best travelling services out there!")

helprequired=input("Would you like to read the help file before starting. (y/n)")

if helprequired == "y" or "yes":
    print("Please wait while the file loads...")
    time.sleep(2)
    help()
else:
    print("Please wait while the program loads")
    time.sleep(2)
    
lastname = input("Please enter your last name: ")
name = input("Please enter your first name: ")
print ("Hello", name, lastname, "hope your day is going well")
address = str(input("Please enter your full address: "))

###LOCATION
print ("""The locations which are available is 
1.Spain
2.Turkey
3.Florida
""")
location=int(input("Please enter the option you would like to travel too: "))
x=1
while x!=0:
    if location ==1:
        print("So you would like to go to Spain.")
        location = "Spain"
        x=x-1
    elif location ==2:
        print("So you would like to go to Turkey.")
        x=x-1
        location = "Turkey"
    elif location ==3:
        print("So you would like to go to Florida.")
        x=x-1
        location = "Florida"
    else:
        print("An error has occured. ")
        location = int(input("Please enter the option: "))

# Duration
import calendar
year = int(input("Please enter the year of the stay: "))
month = int(input("Please enter the number of the month you would like to stay: "))
import time
time.sleep(1)
print(calendar.month(year,month))
print("Please choose the day of the check in.")
dayin= int(input("Please enter the day you would like to check in: "))
dayout=int(input("Please enter the day you would like to check out: "))
def distance(dayin, dayout):
    if dayin >= dayout:
        result = dayin - dayout
    else:
        result = dayout - dayin
    return result
totaldays=(distance(dayin,dayout))

### NUMBER OF GUESTS

guest = int(input("Please enter the amount of people which are going to be staying within the villa: "))
print("Thank you, just putting that through")
time.sleep(1)
print ("There are different types of villas which are available in", location, "")
time.sleep(2)
print("""There are three types of villas available
option 1  2-bed villa (sleeps 6)
option 2  3-bed villa (sleeps 8)
option 3  4-bed villa (sleeps 12)
""")

###VILLAS
x = False
while not x:
    if guest >5 and guest<7:
        global villa
        print("Unfortunately the 2-bed villa is not available.")
        villa=int(input("Please choose from the available options:"))
        x=True
    elif guest >=8 and guest<=10:
        print("You are only accepted for 4-bed villa")
        villa=3
        x=True
    elif guest < 6:
        print("You are accepted for all of the villas.")
        villa=int(input("Please choose from the available options: "))
        x=True
    else:
        ("Unfortunately you are not able to select a villa")
        guest=int(input("Please enter the amount of people which are going to be staying within the villa: "))

### TotalRooms
                  
if villa == 1:
    totalrooms=6
elif villa == 2:
    totalrooms=8
elif villa ==3:
    totalrooms=10

### Car required

car=input("Would you require a car? y/n ")
if car == "y":
    print("Thank you.")
    print("""Small car - £50
          Large car - £80""")
    cartype=input("Which car would you acquire? s/l")
    x = False
    while not x:
        if cartype =="l":
            travel= 100
            x=True
        elif cartype =="n":
            travel = 50
            x=True
        else:
            print("Please try again")
            x=False
            cartype=input("Which car would you acquire? s/l")
else:
    print("""Transfer by coach £20 per person
""")
    coach = input("Would you acquire a coach? y/n")
    if coach =="y":
        print("You have chosen a coach")
        travel = 20 * guest
        print("The total price for the coach is £", travel)
    else:
        print("You have not chosen a coach")
        travel = 0 
### Total
print("Due to the occupancy charge you are going to be charged for rooms which are not being used.")
occupancy = totalrooms-guest
occupancycharge = occupancy * 10
time.sleep(1)
print("The total occupancy charge is £", occupancycharge)
if villa ==1:
    totalvilla = 25.50*totaldays
    print(totalvilla)
elif villa ==2:
    totalvilla = 75.00*totaldays
elif villa ==3:
    totalvilla = 99.95*totaldays
totalprice = totalvilla+occupancycharge+travel
print("Please be patient while we calculate full price")
time.sleep(3)
print("The total is £" + str(totalprice))

information = [name, " ", lastname, " \n",address, "\nThe location user be heading to is ", location]
invoiceprice = ["\nThe total price is £", str(totalprice)]
saveinformation = open("Information.txt","w")
saveinformation.write("Full name is: ")
saveinformation.writelines(information)
saveinformation.writelines (invoiceprice)
saveinformation.close()
os.startfile("Information.txt","print")
