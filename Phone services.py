import time
print("Welcome to SGMC mobile services. ")
time.sleep(1)
name = input("Please enter your name: ")
print("Hello", name, "nice to meet you!")
# print("SGMC offers a range of contracts, or you can make your own one")
# print("")
# customcontract = ("If you would like to make your own contract, please enter 'yes' or 'no' ")
print("if you would like unlimited of a specific service please type the number '0'")
data = int(input("Please enter the amount of data you would like in GB: "))
###Data
if data == 0:
    print ("So you would like unlimited data, this will be noted.")
    data =("Unlimited")
    dataprice = 20
else:
    print ("So you would like", data, "Gb of data!")
    dataprice = data * 2
### Text

text = int(input("Please enter the amount of text you would like:  "))

if text == 0:
    print ("So you would like unlimited text, this will be noted.")
    text =("Unlimited")
    textprice = 5
else:
    print ("So you would like", text, " texts!")
    if text < 1000:
        textprice = 7
    else:
        textprice = 4
### Minute
minutes = int(input("Please enter the amount of minutes you would like: "))

if minutes == 0:
    print ("So you would like unlimited minutes, this will be noted.")
    minutes =("Unlimited")
    minutesprice = 10
else:
    print ("So you would like", minutes, "minutes!")
    if minutes < 1000:
        minutesprice = 10
    else:
        minutesprice = 5

### Finalizing
print("So you would like", data, "GB of data", text, "amount of text", minutes, "amount of minhutes")
###Total price
TotalPrice = dataprice + textprice + minutesprice
print("The total price for the contract is going to be £", TotalPrice ,"we are going to put this through please give us a minute")
time.sleep(2)
print("Thanks it has gone through")
time.sleep(1)
print("Please wait a moment while we print out your invoice")
time.sleep(2)
###Invoice
import turtle
turtle.color("white")
turtle.forward(180)
turtle.color("black")
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(350)
turtle.left(90)
turtle.forward(350)
turtle.left(90)
turtle.forward(350)
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(50)
turtle.right(135)
turtle.forward(1)
turtle.color("white")
turtle.forward(400)
turtle.color("black")
turtle.write("Your total price is £")
turtle.right(135)
turtle.forward(95)
turtle.write(TotalPrice)
time.sleep(3)




### Customer detail
### Mobile phone
### accessories
### payement details
### receipt
### help
### exit
